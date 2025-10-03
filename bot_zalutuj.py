import random
import discord
from discord.ext import commands

# --- KONFIGURACJA ---
import os
TOKEN = os.getenv("DISCORD_TOKEN")
GIF_URL = "https://media.tenor.com/hvRG0cqRsb0AAAAj/coach-josh-coach.gif"
# ---------------------

intents = discord.Intents.default()
intents.members = True  # pozwala botowi pobrać listę członków serwera

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Zalogowano jako {bot.user}!")

@bot.tree.command(name="zalutuj", description="Losowo zalutuj użytkownika 🔧")
async def zalutuj(interaction: discord.Interaction):
    guild = interaction.guild
    if guild is None:
        await interaction.response.send_message("Ta komenda działa tylko na serwerze.", ephemeral=True)
        return

    # pomijamy boty i autora komendy
    members = [m for m in guild.members if not m.bot and m.id != interaction.user.id]
    if not members:
        await interaction.response.send_message("Nie ma nikogo do zalutowania!", ephemeral=True)
        return

    target = random.choice(members)

    embed = discord.Embed(
        title="🔩 Zalutowano!",
        description=f"{interaction.user.mention} zalutował(a) {target.mention}!"
    )
    embed.set_image(url=GIF_URL)

    await interaction.response.send_message(embed=embed)

if __name__ == "__main__":
    bot.run(TOKEN)