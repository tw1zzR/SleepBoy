from discord.ext import commands
from discord import app_commands
import discord
import random
import time
from text_utils import get_verb_for_remaining, format_time_text
from phrases import appeals
from tts import say_gtts
from state import state


class NotifyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.state = state

    @app_commands.command(name="notify", description="Озвучити залишок часу")
    async def notify(self, interaction: discord.Interaction):

        if self.state.sleep_time is None:
            await interaction.response.send_message(f"⏱️ {random.choice(appeals)}, таймер не був встановлений!", ephemeral=True)
            return

        elapsed = time.time() - self.state.start_time
        remaining = self.state.sleep_time - elapsed

        if remaining < 0:
            remaining = 0

        minutes_left = int(remaining // 60)
        seconds_left = int(remaining % 60)

        verb = get_verb_for_remaining(minutes_left // 60, minutes_left % 60, seconds_left)
        text_line, tts_line = format_time_text(minutes_left, seconds_left, context="remaining")

        await interaction.response.send_message(
            f"⏲️ {verb.capitalize()} {text_line}.", ephemeral=False)
        if self.state.voice_client and self.state.voice_client.is_connected():
            await say_gtts(f"{verb.capitalize()} {tts_line}", self.state.voice_client)

async def setup(bot: commands.Bot):
    await bot.add_cog(NotifyCog(bot))