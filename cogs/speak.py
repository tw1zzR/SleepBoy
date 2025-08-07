from discord.ext import commands
from discord import app_commands
import discord
import random
from phrases import appeals
from tts import say_gtts
from state import state


class SpeakCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.state = state

    @app_commands.command(name="speak", description="Озвучити повідомлення")
    @app_commands.describe(message="Повідомлення, яке потрібно озвучити")
    async def speak(self, interaction: discord.Interaction, message: str):

        if self.state.voice_client and self.state.voice_client.is_connected():
            await interaction.response.send_message(f"📢 {message}", ephemeral=True)
            await say_gtts(message, self.state.voice_client)
        else:
            await interaction.response.send_message(f"🤡 я не в голосовому каналі, {random.choice(appeals)} я хуєю..", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(SpeakCog(bot))