import os
from discord import app_commands, Intents, Client, Interaction

class BotDiscord(Client):
    def __init__(self, * intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self) -> None:
        await self.tree.sync(guild=None)

bot = BotDiscord(intents=Intents.default())

@bot.event
async def on_ready():
    print(f"Conected: {bot.user}")

#Test / command
@bot.tree.command()
async def hola(interaction: Interaction):
    await interaction.response.send_message("¡Hola!")

bot.run(os.getenv("DISCORD_TOKEN"))