# HackerNews for Discord

This application fetches and shares top stories from HackerNews for Discord servers. 

It provides automatic hourly updates and allows users to manually fetch news or search for stories by keyword.

## 📢 Features

- Automatic hourly updates of top HackerNews stories
- Manual fetching of top stories
- Keyword search functionality
- User subscription for mentions

## Installation

### ⚙️ Clone Repository

- Clone project files:
```
git clone https://github.com/jntm7/hackernews-discord.git
```
- Navigate to the repo:
```
cd hackernews-discord
```

### ⚙️ Install Required Packages

```
pip install discord.py requests
```

### ⚙️ Assign Discord Token

- Enter your Discord bot token within the `config.py` file:

```python
DISCORD_TOKEN = 'your_discord_bot_token_here'
```

**Note: For security and privacy, never share your Discord bot token in config.py file publicly.**

### ⚙️ Invite Bot to Discord Server

- Invite the bot to your Discord server with the generated OAuth link
- Ensure it has permissions to read messages and send messages in the desired channels.

## ⌨️ Usage

Run the bot with:

```
python main.py
```

## 💭 Commands

- `!sub`: Subscribe to HackerNews updates
- `!unsub`: Unsubscribe from HackerNews updates
- `!news`: Manually fetch and post the top 5 HackerNews stories
- `!search <keyword>`: Search for top 5 stories containing the given keyword

## 🛠️ Setup

- Create a channel named either 'updates' or 'news' in your Discord server.
- The bot will use this channel for automatic hourly updates (while the script is running).
- Users can use the commands in any channel where the bot is present.
