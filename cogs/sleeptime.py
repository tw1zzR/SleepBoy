from discord.ext import commands
from discord import app_commands
import discord
import asyncio
import random
import time
from text_utils import format_time_text
from phrases import appeals
from tts import say_gtts
from state import state


class SleepCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.state = state

    @app_commands.command(name="sleeptime", description="Запустити таймер сну")
    @app_commands.describe(minutes="Кількість хвилин")
    async def sleeptime(self, interaction: discord.Interaction, minutes: int):

        if self.state.sleep_task and not self.state.sleep_task.done():
            await interaction.response.send_message("⛔️ Таймер вже запущено. Щоб його зупинити напиши /stop.", ephemeral=True)
            return

        user_voice = interaction.user.voice
        if not user_voice or not user_voice.channel:
            await interaction.response.send_message(f"🤡 ти не в голосовому каналі, {random.choice(appeals)} блять.", ephemeral=True)
            return

        text_channel = interaction.channel

        self.state.sleep_time = minutes * 60
        self.state.start_time = time.time()

        async def sleep_and_kick():

            if self.state.sleep_time > 300:
                await asyncio.sleep(self.state.sleep_time - 300)
                if self.state.voice_client and self.state.voice_client.is_connected():
                    words = "хвилин і на бокову!"
                    await say_gtts(f"п'ять {words}", self.state.voice_client)
                await text_channel.send(f"⏰ 5 {words}")
                await asyncio.sleep(300)
            else:
                await asyncio.sleep(self.state.sleep_time)

            try:
                self.state.sleep_time = None
                msg2 = "Добраніч, хлопці"
                await say_gtts(msg2, self.state.voice_client)
                await text_channel.send(f"💤 {msg2}")
                await asyncio.sleep(5)
            except:
                pass

            for member in user_voice.channel.members:
                if not member.bot:
                    try:
                        await member.move_to(None)
                    except:
                        pass

            async def disable_night_mode():
                self.state.night_mode = True
                await asyncio.sleep(120)
                self.state.night_mode = False

                if self.state.voice_client and self.state.voice_client.is_connected():
                    await self.state.voice_client.disconnect()
                    self.state.voice_client = None

            asyncio.create_task(disable_night_mode())
            self.state.sleep_task = None

        if self.state.sleep_task and not self.state.sleep_task.done():
            self.state.sleep_task.cancel()

        self.state.sleep_task = asyncio.create_task(sleep_and_kick())

        text_line, tts_line = format_time_text(minutes, context="started")
        await interaction.response.send_message(f"🕒 Таймер запущено на {text_line}.", ephemeral=False)
        if self.state.voice_client and self.state.voice_client.is_connected():
            await say_gtts(f"Таймер запущено на {tts_line}", self.state.voice_client)

async def setup(bot: commands.Bot):
    await bot.add_cog(SleepCog(bot))