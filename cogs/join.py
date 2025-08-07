from discord.ext import commands
from discord import app_commands
import discord
import random
from phrases import greetings, appeals
from tts import say_gtts
from state import state


class JoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.state = state

    @app_commands.command(name="join", description="Зайти в голосовий канал")
    async def join(self, interaction: discord.Interaction):

        user_voice = interaction.user.voice
        if not user_voice or not user_voice.channel:
            await interaction.response.send_message(f"🤡 {random.choice(appeals)} ти навіть не в голосовому каналі!", ephemeral=True)
            return

        channel = user_voice.channel

        if interaction.guild.voice_client:
            await interaction.response.send_message(f"☝️ я вже сиджу з пациками в {channel.name}!", ephemeral=True)
            return

        try:
            vc = await channel.connect()
            if vc.is_connected():
                self.state.voice_client = vc
                await interaction.response.send_message(f"🍻 Зайшла в голосовий канал {channel.name}.", ephemeral=False)
                await say_gtts(random.choice(greetings), self.state.voice_client)
        except discord.ClientException:
            pass

async def setup(bot: commands.Bot):
    await bot.add_cog(JoinCog(bot))