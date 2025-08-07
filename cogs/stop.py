from discord.ext import commands
from discord import app_commands
import discord
from state import state


class StopCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.state = state

    @app_commands.command(name="stop", description="Зупинити таймер сну")
    async def stop(self, interaction: discord.Interaction):

        if self.state.sleep_task and not self.state.sleep_task.done():
            self.state.sleep_task.cancel()
            self.state.sleep_task = None
            self.state.sleep_time = None
            self.state.start_time = None
            await interaction.response.send_message("🛑 Таймер було зупинено.", ephemeral=False)
        else:
            await interaction.response.send_message("😴 Немає активного таймера.", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(StopCog(bot))