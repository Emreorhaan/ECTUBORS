import discord
from discord.ext import commands
import cekemeyenler_utansin as cu
import datetime


class kurBilgisi(commands.Cog):
	def __init__(self,bot):
		pass
		
	
	@commands.command()
	async def yardim(self, message):
		embed=discord.Embed(title="KOMUTLAR", description="============", color=0x00ffff)
		embed.add_field(name="e!kur", value="Bazı para birimlerinin ve değerli madenlerin değerlerini gösterir", inline=False)
		embed.add_field(name="e!coin", value="Bazı kripto paraların değerlerini gösterir", inline=False)
		embed.add_field(name="e! + coin ismi", value="Örnek: e!btc, e!eth, e!avax", inline=False)
		await message.send(embed=embed)
		
		
	@commands.command()
	async def kur(self, message):
		cu.kurcek()
		dolar = cu.dolar()[1] + " TL || " + cu.dolar()[3]+"%"
		euro = cu.euro()[1] + " TL || " + cu.euro()[3]+"%"
		altin = cu.altin()[1] + " TL || " + cu.altin()[3]+"%"
		
		tarih = datetime.datetime.now()
		
		tarih = str(tarih.hour) +"."+ str(tarih.minute) +"  "+ str(tarih.day) +"."+ str(tarih.month) +"."+ str(tarih.year)
		
		embed=discord.Embed(title = "EKONOMİ" ,color=0x00ffff)
		embed.add_field(name="Dolar :dollar:", value=dolar, inline=False)
		embed.add_field(name="Euro :euro:", value=euro, inline=False)
		embed.add_field(name="Altın :yellow_circle:", value=altin, inline=False)
		embed.set_footer(text="Son Güncelleme Tarihi: "+tarih)
		await message.send(embed=embed)
		
	@commands.command()
	async def coin(self, message):

		tarih = datetime.datetime.now()
		
		tarih = str(tarih.hour) +"."+ str(tarih.minute) +"  "+ str(tarih.day) +"."+ str(tarih.month) +"."+ str(tarih.year)
		
		btc = cu.coin("BTCUSDT")
		eth = cu.coin("ETHUSDT")
		ada = cu.coin("ADAUSDT")
		bnb = cu.coin("BNBUSDT")
		dot = cu.coin("DOTUSDT")
		avax = cu.coin("AVAXUSDT")
		xrp = cu.coin("XRPUSDT")
		link = cu.coin("LINKUSDT")
						
		embed=discord.Embed(title="KRİPTO PARA PİYASASI", color=0x00ffff)
		embed.add_field(name="BTC", value=btc + "$", inline=False)
		embed.add_field(name="ETH", value=eth + "$", inline=False)
		embed.add_field(name="ADA", value=ada+"$", inline=False)
		embed.add_field(name="BNB", value=bnb+"$", inline=False)
		embed.add_field(name="DOT", value=dot+"$", inline=False)
		embed.add_field(name="AVAX", value=avax+"$", inline=False)
		embed.add_field(name="XRP", value=xrp+"$", inline=False)
		embed.add_field(name="LINK", value=link+"$", inline=False)
		embed.set_footer(text="Son Güncelleme Tarihi: "+tarih)
		await message.send(embed=embed)
		
	@commands.command()
	async def btc(self,message):
		await message.send("BTC: "+cu.coin("BTCUSDT")+"$")
		
	@commands.command()
	async def eth(self,message):
		await message.send("ETH: "+cu.coin("ETHUSDT")+"$")
		
	@commands.command()
	async def ada(self,message):
		await message.send("ADA: "+cu.coin("ADAUSDT")+"$")
		
	@commands.command()
	async def bnb(self,message):
		await message.send("BNB: "+cu.coin("BNBUSDT")+"$")
		
	@commands.command()
	async def avax(self,message):
		await message.send("AVAX: "+cu.coin("AVAXUSDT")+"$")
		
	@commands.command()
	async def dot(self,message):
		await message.send("DOT: "+cu.coin("DOTUSDT")+"$")
		
	@commands.command()
	async def xrp(self,message):
		await message.send("XRP: "+cu.coin("XRPUSDT")+"$")
		
	@commands.command()
	async def link(self,message):
		await message.send("LINK: "+cu.coin("LINKUSDT")+"$")

	
def setup(bot):
		bot.add_cog(kurBilgisi(bot))
