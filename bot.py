import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

class TradeView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="📩 Open Middleman Ticket", style=discord.ButtonStyle.blurple, custom_id="open_ticket_btn")
    async def button_callback(self, interaction: discord.Interaction, button: discord.Button):
        guild = interaction.guild
        member = interaction.user
        
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            member: discord.PermissionOverwrite(view_channel=True, send_messages=True),
            guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True)
        }
        
        ticket_channel = await guild.create_text_channel(name=f"ticket-{member.name}", overwrites=overwrites)
        
        embed = discord.Embed(
            title="🎯 Middleman & Trade Ticket",
            description=f"Welcome {member.mention},\n\nThis private room has been successfully opened to complete your trade securely.\nPlease wait for the Middleman to assist you, and do not share any sensitive details outside this channel.",
            color=discord.Color.green()
        )
        await ticket_channel.send(embed=embed)
        await interaction.response.send_message(f"Your ticket has been opened successfully in: {ticket_channel.mention}", ephemeral=True)

@bot.event
async def on_ready():
    print(f"Logged in successfully as: {bot.user}")
    bot.add_view(TradeView())

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_panel(ctx):
    embed = discord.Embed(
        title="🌐 Secure Trading & Middleman System",
        description="Click the button below to open a private ticket and start your trade with an official Middleman.\n\n⚡ **Warning:** Do not trade via Direct Messages (DMs) to protect your accounts.",
        color=discord.Color.gold()
    )
    await ctx.send(embed=embed, view=TradeView())

bot.run('MTUxNjIyODExMjIxNDM5NzA1OA.GhRnMR.tw8GxASaB3ZkL1EHfbS74b3lw4auIBiMwN_-cI')
