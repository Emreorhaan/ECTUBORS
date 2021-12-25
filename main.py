import discord
from discord.ext import commands

token = "ODkxNjkxNzQ3OTI1Njg4NDMx.YVCCpw.Wk9NkE9wLc22G3l-Lo0Q9pfU6YI"

class Bot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix = "e!", pm_help = None, )
		
		self.load_extension("kur")
		
	async def on_ready(self):
		print("Bot Açıldı")
	
bot = Bot()
bot.run(token)

