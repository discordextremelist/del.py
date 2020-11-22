# DEL.py
#### The official Python Library for the [discordextremelist.xyz](https://discordextremelist.xyz) API

# Installation

### pypi (recommended) (not on pypi yet)
#### `pip install del.py`
### source
#### `pip install git+https://github.com/discordextremelist/del.py`

# Code Examples

## Post bot stats (server count, shard count): *you might need to change loop*

```python
import delpy

from discord.ext import commands, tasks

class discordextremelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_stats.start()
        self.delapi = delpy.Client("token", loop=bot.loop)  # you can get token from your bot page on DEL

    def cog_unload(self):
        self.update_stats.cancel()

    @tasks.loop(minutes=30.0)
    async def update_stats(self):
        try:
            await self.delapi.post_stats(botid=str(self.bot.user.id), guildCount=len(self.bot.guilds), shardCount=len(self.bot.shards))  # You can remove shardCount
        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(discordextremelist(bot))
```

## Get server/bot/template/user information

```python
import delpy

from discord.ext import commands

class discordextremelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.delapi = delpy.Client(loop=bot.loop)  # you might need to change loop
    
    # you can either make a command or anything you want
    # you'll need to use this line inside your command though
    # data = await self.delapi.get_{option}_info("<id goes here>")
    # valid options: server, bot, template, user

def setup(bot):
    bot.add_cog(discordextremelist(bot))
```

## Get website statistics/health

```python
import delpy

from discord.ext import commands

class discordextremelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.delapi = delpy.Client(loop=bot.loop)  # you might need to change loop
    
    # you can either make a command or anything you want
    # you'll need to use this line inside your command though
    # data = await self.delapi.get_website_{option}()
    # valid options: health, stats

def setup(bot):
    bot.add_cog(discordextremelist(bot))
```

### If you're lost, do not hesitate and join [del server](https://discord.gg/WeCer3J) where you can ask for help in #development