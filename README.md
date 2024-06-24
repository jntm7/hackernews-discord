# HackerNews Discord Bot

This application fetches and shares top stories from HackerNew for Discord servers. It provides automatic hourly updates and allows users to manually fetch news or search for stories by keyword.

## Features

- Automatic hourly updates of top HackerNews stories
- Manual fetching of top stories
- Keyword search functionality
- User subscription system for mentions

## Installation

### 1. Clone this repository:

```git clone https://github.com/yourusername/hackernews-discord-bot.git
cd hackernews-discord-bot
```

### 2. Install the required packages:

```
pip install discord.py requests
```

### 3. Create a `config.py` file in the root directory with your Discord bot token:

```python
DISCORD_TOKEN = 'your_discord_bot_token_here'
```

**Note: For security and privacy, never share your Discord bot token in config.py file publicly.**

### 4. Invite the bot to your Discord server and ensure it has permissions to read messages and send messages in the desired channels.

## Usage

Run the bot with:

```
python hackernews_bot.py
```

## Commands

`!sub`: Subscribe to HackerNews updates
`!unsub`: Unsubscribe from HackerNews updates
`!news`: Manually fetch and post the top 5 HackerNews stories
`!search <keyword>`: Search for top 3 stories containing the given keyword

## Setup

- Create a channel named either 'updates' or 'news' in your Discord server. The bot will use this channel for automatic hourly updates (while the script is running).
- Users can use the commands in any channel where the bot is present.