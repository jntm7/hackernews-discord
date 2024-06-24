import requests
import discord
from discord.ext import commands, tasks
from config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

subscribed_users = set()

def get_top_stories(num_stories=5):
    try:
        response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
        response.raise_for_status()
        top_story_ids = response.json()[:num_stories]
        
        stories = []
        for id in top_story_ids:
            story_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json")
            story_response.raise_for_status()
            story_data = story_response.json()
            stories.append(story_data)
        
        return stories
    except Exception as e:
        print(f"Error fetching stories: {e}")
        return []

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    scheduled_news.start()

@bot.command(name='sub')
async def subscribe(ctx):
    subscribed_users.add(ctx.author.id)
    await ctx.send("You've subscribed to HackerNews updates!")

@bot.command(name='unsub')
async def unsubscribe(ctx):
    subscribed_users.discard(ctx.author.id)
    await ctx.send("You've unsubscribed from HackerNews updates.")

@bot.command(name='news')
async def fetch_news(ctx):
    await send_top_stories(ctx.channel)

@bot.command(name='search')
async def search_news(ctx, keyword: str):
    stories = get_top_stories(5)
    matching_stories = [s for s in stories if keyword.lower() in s.get('title', '').lower()][:3]
    
    if matching_stories:
        for story in matching_stories:
            embed = create_story_embed(story)
            await ctx.send(embed=embed)
    else:
        await ctx.send(f"No stories found matching '{keyword}'.")

def create_story_embed(story):
    embed = discord.Embed(
        title=story.get('title', 'No title'),
        url=story.get('url', ''),
        description=f"Score: {story.get('score', 'N/A')} | Comments: {story.get('descendants', 'N/A')}",
        color=discord.Color.orange()
    )
    embed.set_author(name="Hacker News", icon_url="https://news.ycombinator.com/favicon.ico")
    return embed

async def send_top_stories(channel=None):
    if channel is None:
        channel = discord.utils.get(bot.get_all_channels(), name='updates') or discord.utils.get(bot.get_all_channels(), name='news')
    
    if channel:
        stories = get_top_stories()
        if stories:
            if subscribed_users:
                mentions = ' '.join([f'<@{user_id}>' for user_id in subscribed_users])
                await channel.send(f"New HackerNews stories for: {mentions}")
            
            for story in stories:
                embed = create_story_embed(story)
                await channel.send(embed=embed)
    else:
        print("Couldn't find 'updates' or 'news' channel.")

@tasks.loop(hours=1)
async def scheduled_news():
    await send_top_stories()

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)