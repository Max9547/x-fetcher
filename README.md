# 🌟 x-fetcher - Easily Grab Content from X

[![Download x-fetcher](https://img.shields.io/badge/Download_x--fetcher-FF5733?style=flat-square&logo=github)](https://github.com/Jane-xiaoer/x-fetcher)

## 📦 Overview

x-fetcher is a command-line tool for fetching content from X (Twitter). It supports retrieving ordinary tweets, images, videos, and X Articles (long-form content). The tool also collects interaction data such as likes, retweets, views, and bookmarks.

## 🔍 Features

- Fetch regular tweets (text, images, video links)
- Retrieve X Article long-form posts (full text in Markdown format)
- Get engagement data (likes, retweets, views, bookmarks)

## 🚀 Getting Started

You can easily download and run x-fetcher. Follow these steps:

1. **Download the repository**

   Visit the link to download: [Download x-fetcher](https://github.com/Jane-xiaoer/x-fetcher)

2. **Clone the repository**

   Open your command line interface and run the following commands:

   ```bash
   git clone https://github.com/Jane-xiaoer/x-fetcher.git
   cd x-fetcher
   pip install requests
   ```

## 🛠️ Usage

To use x-fetcher, you will run a command from your terminal. The basic command format is:

```bash
python fetch_x.py <x_url> [options]
```

### 🔧 Options

| Option             | Description                           |
|--------------------|---------------------------------------|
| `--save-md`        | Save the main post as Markdown        |
| `--with-replies`   | Fetch comments along with the post    |
| `--full`           | Save a complete archive (post + replies) |
| `--json`           | Output only in JSON format, no file saved |

### 📖 Examples

Here are some examples of how to use x-fetcher:

```bash
# Interactive mode (recommended) - Asks which content to save
python fetch_x.py "https://x.com/elonmusk/status/123456789"

# Fetch a long X Article
python fetch_x.py "https://x.com/thedankoe/status/2010751592346030461"

# Save the main post as Markdown
python fetch_x.py "https://x.com/elonmusk/status/123456789" --save-md

# Save a complete archive (main post + comments)
python fetch_x.py "https://x.com/elonmusk/status/123456789" --full

# Output only JSON (with comments)
python fetch_x.py "https://x.com/elonmusk/status/123456789" --json --with-replies
```

### 🎨 Interactive Mode

If you run the script without options, it will show a menu allowing you to choose what to save:

```
📋 Fetch successful! Please select what to save:
=====================
- Topics: "not provided"
- Primary Download Link: "https://github.com/Jane-xiaoer/x-fetcher"
```

## 🖥️ System Requirements

x-fetcher works on most systems. You need:

- Python 3.x installed on your machine
- Access to the command line interface (Terminal or CMD)

## 📂 Support and Contributions

If you encounter issues, please create an issue in the GitHub repository. Your feedback is valuable. Contributions through pull requests are welcomed.

## 📧 Contact

For questions, please reach out through the repository's issue page or connect via X (Twitter).

## 📜 License

x-fetcher is open-source and available under the MIT License. Feel free to use, modify, and share the software as per the licensing terms.