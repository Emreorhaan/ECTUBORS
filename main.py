import discord
from discord.ext import commands

token = "IDElnL9ELNmqiL4_a4S-aritKoqNiect"

class Bot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix = "e!", pm_help = None, )
		
		self.load_extension("kur")
		
	async def on_ready(self):
		print("Bot Açıldı")
	
bot = Bot()
bot.run(token)

