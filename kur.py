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
		altin = cu.altin()[1] + " TL || " + cu.altin()[3]
		
		tarih = datetime.datetime.now()
		
		tarih = str(tarih.hour) +"."+ str(tarih.minute) +"  "+ str(tarih.day) +"."+ str(tarih.month) +"."+ str(tarih.year)
		
		embed=discord.Embed(title = "EKONOMİ" ,color=0x00ffff)
		embed.add_field(name="Dolar :dollar:", value=dolar, inline=False)
		embed.add_field(name="Euro :euro:", value=euro, inline=False)
		embed.add_field(name="Altın :yellow_circle:", value=altin, inline=False)
		embed.set_footer(text="Son Güncelleme Tarihi: "+tarih)
		await message.send(embed=embed)
		
	@commands.command()
	async def coins(self, message):

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
	async def coin(self, message, *args):
		if len(args) == 2:
			try:
				coininfo = cu.coin(args[0].upper()+"USDT")
				coininfo = coininfo[0:7]
				
				await message.send(args[1] +" "+args[0].upper()+": "+str(float(coininfo) * float(args[1]))+"$")
			
			except:
				await message.send("Hatalı Komut")
		else:
			coininfo = cu.coin(args[0].upper()+"USDT")
			coininfo = coininfo[0:7]
			await message.send(args[0].upper()+": "+coininfo+"$")

	
def setup(bot):
		bot.add_cog(kurBilgisi(bot))
