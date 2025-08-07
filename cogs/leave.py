from discord.ext import commands
from discord import app_commands
import discord
import random
from phrases import farewells, appeals
from tts import say_gtts
from state import state


class LeaveCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.state = state

    @app_commands.command(name="leave", description="Вийти з голосового каналу")
    async def leave(self, interaction: discord.Interaction):

        async with self.state.async_lock:
            local_voice = self.state.voice_client
            if local_voice and local_voice.is_connected():
                await interaction.response.send_message(
                    f"👣 Вийшла з голосового каналу {interaction.user.voice.channel}.", ephemeral=False)
                await say_gtts(random.choice(farewells), local_voice)
                try:
                    await local_voice.disconnect()
                except Exception:
                    pass
                self.state.voice_client = None
            else:
                await interaction.response.send_message(f"🤡 я не в голосовому каналі, {random.choice(appeals)}!", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(LeaveCog(bot))