from dotenv import load_dotenv
from discord.ext import commands
import discord
import asyncio
import os
from tts import cleanup_tts_files, periodic_cleanup
from state import state


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)
        self.state = state

    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
        await self.tree.sync()

bot = MyBot()

@bot.event
async def on_ready():
    print(f'Bot launched as {bot.user}')
    cleanup_tts_files()
    asyncio.create_task(periodic_cleanup())

@bot.event
async def on_voice_state_update(member, before, after):

    if state.night_mode and after.channel is not None:
        try:
            await member.move_to(None)
            channel = bot.get_channel(1402319150470140207)
            await channel.send(f"🖕 <@{member.id}> ало вася, йди спать")
        except Exception:
            pass

bot.run(TOKEN)