from discord.ext import commands
from . import emote

def is_bot_setuped():
    async def predicate(ctx):
        if ctx.guild is None:
            return False

        data = await ctx.db.fetchval('SELECT is_bot_setuped FROM server_configs WHERE guild_id = $1',ctx.guild.id)
        if data is False:
            await ctx.send(f'{emote.error} | This Server Does Not Have the BotSetup Here Use `,setup`')
            False
            return

        return True
    return commands.check(predicate)

def is_smanager_setuped():
    async def predicate(ctx):
        if ctx.guild is None:
            return False

        data = await ctx.db.fetchval('SELECT scrims_manager FROM server_configs WHERE guild_id = $1',ctx.guild.id)
        if data is False:
            await ctx.send(f'{emote.error} | This Server Does Not Have Smanager Setup Use `,smanager setup`')
            False
            return

        return True
    return commands.check(predicate)