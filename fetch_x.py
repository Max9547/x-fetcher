#!/usr/bin/env python3
"""
X (Twitter) 帖子内容抓取工具
支持普通推文和 X Article 长文章
用法: python fetch_x.py <x_url>
"""

import sys
import re
import json
import requests
from urllib.parse import urlparse

def extract_tweet_id(url):
    """从 URL 提取 tweet ID"""
    patterns = [
        r'(?:x\.com|twitter\.com)/\w+/status/(\d+)',
        r'(?:x\.com|twitter\.com)/\w+/statuses/(\d+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def extract_username(url):
    """从 URL 提取用户名"""
    match = re.search(r'(?:x\.com|twitter\.com)/(\w+)/status', url)
    return match.group(1) if match else None

def fetch_via_fxtwitter(url):
    """通过 fxtwitter API 获取内容"""
    api_url = re.sub(r'(x\.com|twitter\.com)', 'api.fxtwitter.com', url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    try:
        resp = requests.get(api_url, headers=headers, timeout=15)
        if resp.status_code == 200:
            return resp.json()
    except Exception as e:
        print(f"  fxtwitter 错误: {e}", file=sys.stderr)
    return None

def fetch_via_syndication(tweet_id):
    """通过 X 的 syndication API 获取内容"""
    url = f"https://cdn.syndication.twimg.com/tweet-result?id={tweet_id}&token=0"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            return resp.json()
    except Exception as e:
        print(f"  syndication 错误: {e}", file=sys.stderr)
    return None

def extract_article_content(article):
    """从 X Article 中提取完整内容"""
    if not article:
        return None

    content_blocks = article.get("content", {}).get("blocks", [])

    # 拼接所有文本块
    paragraphs = []
    for block in content_blocks:
        text = block.get("text", "").strip()
        block_type = block.get("type", "unstyled")

        if text:
            # 根据类型添加格式
            if block_type == "header-one":
                paragraphs.append(f"# {text}")
            elif block_type == "header-two":
                paragraphs.append(f"## {text}")
            elif block_type == "header-three":
                paragraphs.append(f"### {text}")
            elif block_type == "blockquote":
                paragraphs.append(f"> {text}")
            elif block_type == "unordered-list-item":
                paragraphs.append(f"- {text}")
            elif block_type == "ordered-list-item":
                paragraphs.append(f"1. {text}")
            else:
                paragraphs.append(text)

    return "\n\n".join(paragraphs)

def format_output(data, source):
    """格式化输出"""
    result = {
        "source": source,
        "success": True,
        "type": "tweet",
        "content": {}
    }

    if source == "fxtwitter":
        tweet = data.get("tweet", {})
        article = tweet.get("article")

        if article:
            # X Article 长文章
            result["type"] = "article"
            result["content"] = {
                "title": article.get("title", ""),
                "preview": article.get("preview_text", ""),
                "full_text": extract_article_content(article),
                "cover_image": article.get("cover_media", {}).get("media_info", {}).get("original_img_url"),
                "author": tweet.get("author", {}).get("name", ""),
                "username": tweet.get("author", {}).get("screen_name", ""),
                "created_at": article.get("created_at", ""),
                "modified_at": article.get("modified_at", ""),
                "likes": tweet.get("likes", 0),
                "retweets": tweet.get("retweets", 0),
                "views": tweet.get("views", 0),
                "bookmarks": tweet.get("bookmarks", 0)
            }
        else:
            # 普通推文
            result["content"] = {
                "text": tweet.get("text", ""),
                "author": tweet.get("author", {}).get("name", ""),
                "username": tweet.get("author", {}).get("screen_name", ""),
                "created_at": tweet.get("created_at", ""),
                "likes": tweet.get("likes", 0),
                "retweets": tweet.get("retweets", 0),
                "views": tweet.get("views", 0),
                "media": [m.get("url") for m in tweet.get("media", {}).get("all", []) if m.get("url")],
                "replies": tweet.get("replies", 0)
            }

    elif source == "syndication":
        result["content"] = {
            "text": data.get("text", ""),
            "author": data.get("user", {}).get("name", ""),
            "username": data.get("user", {}).get("screen_name", ""),
            "created_at": data.get("created_at", ""),
            "likes": data.get("favorite_count", 0),
            "retweets": data.get("retweet_count", 0),
            "media": [m.get("media_url_https") for m in data.get("mediaDetails", []) if m.get("media_url_https")]
        }

    return result

def fetch_tweet(url):
    """主函数：尝试多种方式获取帖子内容"""
    tweet_id = extract_tweet_id(url)
    username = extract_username(url)

    if not tweet_id:
        return {"success": False, "error": "无法从 URL 提取 tweet ID"}

    print(f"📍 Tweet ID: {tweet_id}", file=sys.stderr)
    print(f"📍 Username: {username}", file=sys.stderr)
    print(f"🔍 正在抓取...", file=sys.stderr)

    # 方法1: fxtwitter API (支持 Article)
    print("  尝试 fxtwitter API...", file=sys.stderr)
    data = fetch_via_fxtwitter(url)
    if data and data.get("tweet"):
        print("  ✅ fxtwitter 成功", file=sys.stderr)
        return format_output(data, "fxtwitter")

    # 方法2: syndication API
    print("  尝试 syndication API...", file=sys.stderr)
    data = fetch_via_syndication(tweet_id)
    if data and data.get("text"):
        print("  ✅ syndication 成功", file=sys.stderr)
        return format_output(data, "syndication")

    return {"success": False, "error": "所有抓取方式均失败"}

def main():
    if len(sys.argv) < 2:
        print("用法: python fetch_x.py <x_url>")
        print("示例: python fetch_x.py https://x.com/elonmusk/status/123456789")
        sys.exit(1)

    url = sys.argv[1]
    result = fetch_tweet(url)

    # 输出 JSON 结果
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
