---
description: A page to list all the examples on how to use the package.
---

# Example Usage

## Examples

{% hint style="info" %}
The logger is only available for posting, not fetching the data
{% endhint %}

### Automatic data posting

```python
import delpy
import logging

from discord.ext import commands, tasks
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('del.py')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(
    filename='path/to/prefered/log_dir/del.log',
    encoding='utf-8',
    mode='w',
    maxBytes=10 * 1024 * 1024,  # 10 MB
    backupCount=5,
    delay=0
)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class discordextremelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_stats.start()
        # you can get the bot's token from your bot's page on DEL
        self.delapi = delpy.Client(bot, "DELAPI_32chartoken-userid") 
        self.delapi.start_loop(wait_for=1800) # wait_for argument is optional and defaults at 1800.

    def cog_unload(self):
        self.delapi.close_loop()

def setup(bot):
    bot.add_cog(discordextremelist(bot))
```

## Manual data posting

```python
import delpy
import logging

from discord.ext import commands, tasks
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('del.py')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler(
    filename='path/to/prefered/log_dir/del.log',
    encoding='utf-8',
    mode='w',
    maxBytes=10 * 1024 * 1024,  # 10 MB
    backupCount=5,
    delay=0
)
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class discordextremelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_stats.start()
        self.delapi = delpy.Client(bot, "DELAPI_32chartoken-userid")  # you can get the token from your bot's page on DEL

    def cog_unload(self):
        self.update_stats.cancel()

    @tasks.loop(minutes=30.0)
    async def update_stats(self):
        try:
            await self.delapi.post_stats(guildCount=len(self.bot.guilds), shardCount=len(self.bot.shards))  # shardCount is optional
        except Exception as e:
            print(e)  # you can also log in the discord channel instead of printing.

def setup(bot):
    bot.add_cog(discordextremelist(bot))
```

## Get information about bot/template/server/user

```python
import delpy

from discord.ext import commands

class discordextremelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.delapi = delpy.Client()
    
    # you can either make a command or anything you want
    # you'll need to use this line inside your command though
    # data = await self.delapi.get_{option}_info("<id goes here>")
    # valid options: server, bot, template, user

def setup(bot):
    bot.add_cog(discordextremelist(bot))
```

## Get website's statistics/health

```python
import delpy

from discord.ext import commands

class discordextremelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.delapi = delpy.Client()
    
    # you can either make a command or anything you want
    # you'll need to use this line inside your command though
    # data = await self.delapi.get_website_{option}()
    # valid options: health, stats

def setup(bot):
    bot.add_cog(discordextremelist(bot))
```

