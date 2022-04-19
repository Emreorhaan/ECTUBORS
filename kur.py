import discord
from discord.ext import commands
import cekemeyenler_utansin as c
import datetime


class kurBilgisi(commands.Cog):
	def __init__(self,bot):
		pass
		
	
	@commands.command()
	async def yardim(self, message):
		embed=discord.Embed(title="KOMUTLAR", description="============", color=0x00ffff)
		embed.add_field(name="e!kur", value="Bazı para birimlerinin ve değerli madenlerin değerlerini gösterir", inline=False)
		embed.add_field(name="e!akaryakıt", value="İstanbul avrupa bölgesindeki anlık akaryakıt fiyatlarını gösterir", inline=False)
		embed.add_field(name="e!akaryakıt (il)", value="İstenilen ilin karyakıt fiyatlarını gösterir", inline=False)
		embed.add_field(name="e!coins", value="Bazı kripto paraların değerlerini gösterir", inline=False)
		embed.add_field(name="e!coin + coin ismi", value="Örnek: e!coin btc", inline=False)
		embed.add_field(name="e!coin + coin ismi + adet", value="Örnek: e!coin btc 2", inline=False)
		await message.send(embed=embed)
		
		
	@commands.command()
	async def kur(self, message):
		
			
		dolar = c.dolar()[1] + " ₺ || " + c.dolar()[3]+"%"
		euro = c.euro()[1] + " ₺ || " + c.euro()[3]+"%"
		altin = c.altin()[1] + " ₺ || " + c.altin()[3].replace("%","") + "%"
		hisse = c.hisse()[0] + " ₺ || " + c.hisse()[1].replace("%","") + "%"
		petrol = c.petrol()[0] + " $ || " + c.petrol()[1].replace("%","") + "%"
		
		tarih = datetime.datetime.now()
		saat = tarih.hour
		
		tarih = str(saat) +"."+ str(tarih.minute) +"  "+ str(tarih.day) +"."+ str(tarih.month) +"."+ str(tarih.year)
		
		embed=discord.Embed(title = "EKONOMİ" ,color=0x00ffff)
		embed.add_field(name="Dolar :dollar:", value=dolar, inline=False)
		embed.add_field(name="Euro :euro:", value=euro, inline=False)
		embed.add_field(name="Altın :yellow_circle:", value=altin, inline=False)
		embed.add_field(name="Bist 100 :regional_indicator_b: ", value=hisse, inline=False)
		embed.add_field(name="Petrol :oil: ", value=petrol, inline=False)
		embed.set_footer(text="Son Güncelleme Tarihi: "+tarih)
		await message.send(embed=embed)
		
	@commands.command()
	async def coins(self, message):

		tarih = datetime.datetime.now()
		saat = tarih.hour
		
		tarih = str(saat) +"."+ str(tarih.minute) +"  "+ str(tarih.day) +"."+ str(tarih.month) +"."+ str(tarih.year)
		
		btc = c.coin("BTCUSDT")
		eth = c.coin("ETHUSDT")
		ada = c.coin("ADAUSDT")
		bnb = c.coin("BNBUSDT")
		dot = c.coin("DOTUSDT")
		avax = c.coin("AVAXUSDT")
		xrp = c.coin("XRPUSDT")
		link = c.coin("LINKUSDT")
						
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
				coininfo = c.coin(args[0].upper()+"USDT")
				coininfo = coininfo[0:7]
				
				await message.send(args[1] +" "+args[0].upper()+": "+str(float(coininfo) * float(args[1]))+"$")
			
			except:
				await message.send("Hatalı Komut")
		else:
			coininfo = c.coin(args[0].upper()+"USDT")
			coininfo = coininfo[0:7]
			await message.send(args[0].upper()+": "+coininfo+"$")

	@commands.command()
	async def akaryakıt(self, message, *args):

		if len(args) == 1:
			try:
				_akaryakıt_bilgi = c.akaryakıt_il(args[0])
				
				_il = _akaryakıt_bilgi
			
			except:
				await message.send("Hatalı Komut")

			il = _il["Il"]
			kursunsuz = _il["K95"] + " ₺ "
			dizel = _il["Mot50"] + " ₺ "
			prodizel = _il["MotPro"] + " ₺ "
			lpg = _il["PoGaz"] + " ₺ "
		
		
			tarih = datetime.datetime.now()
			saat = tarih.hour
		
			tarih = str(saat) +"."+ str(tarih.minute) +"  "+ str(tarih.day) +"."+ str(tarih.month) +"."+ str(tarih.year)
		
			embed=discord.Embed(title = f"{il} Fiyatları Gösterilmektedir" ,color=0x00ffff)
			embed.add_field(name="Kurşunsuz 95: ", value=kursunsuz, inline=False)
			embed.add_field(name="Diesel: ", value=dizel, inline=False)
			embed.add_field(name="Pro Diesel: ", value=prodizel, inline=False)
			embed.add_field(name="LPG: ", value=lpg, inline=False)
			embed.set_footer(text="Son Güncelleme Tarihi: "+tarih)
			await message.send(embed=embed)
		else:
			kursunsuz = c.akaryakıt("K95") + " ₺ "
			dizel = c.akaryakıt("Mot50") + " ₺ "
			prodizel = c.akaryakıt("MotPro") + " ₺ "
			lpg = c.akaryakıt("PoGaz") + " ₺ "
		
		
			tarih = datetime.datetime.now()
			saat = tarih.hour
		
			tarih = str(saat) +"."+ str(tarih.minute) +"  "+ str(tarih.day) +"."+ str(tarih.month) +"."+ str(tarih.year)
		
			embed=discord.Embed(title = "İstanbul Avrupa Fiyatları Baz Alınmıştır" ,color=0x00ffff)
			embed.add_field(name="Kurşunsuz 95: ", value=kursunsuz, inline=False)
			embed.add_field(name="Diesel: ", value=dizel, inline=False)
			embed.add_field(name="Pro Diesel: ", value=prodizel, inline=False)
			embed.add_field(name="LPG: ", value=lpg, inline=False)
			embed.set_footer(text="Son Güncelleme Tarihi: "+tarih)
			await message.send(embed=embed)
	
	@commands.command()
	async def akaryakit(self, message, *args):

		if len(args) == 1:
			try:
				_akaryakıt_bilgi = c.akaryakıt_il(args[0])
				
				_il = _akaryakıt_bilgi
			
			except:
				await message.send("Hatalı Komut")

			il = _il["Il"]
			kursunsuz = _il["K95"] + " ₺ "
			dizel = _il["Mot50"] + " ₺ "
			prodizel = _il["MotPro"] + " ₺ "
			lpg = _il["PoGaz"] + " ₺ "
		
		
			tarih = datetime.datetime.now()
			saat = tarih.hour
		
			tarih = str(saat) +"."+ str(tarih.minute) +"  "+ str(tarih.day) +"."+ str(tarih.month) +"."+ str(tarih.year)
		
			embed=discord.Embed(title = f"{il} Fiyatları Gösterilmektedir" ,color=0x00ffff)
			embed.add_field(name="Kurşunsuz 95: ", value=kursunsuz, inline=False)
			embed.add_field(name="Diesel: ", value=dizel, inline=False)
			embed.add_field(name="Pro Diesel: ", value=prodizel, inline=False)
			embed.add_field(name="LPG: ", value=lpg, inline=False)
			embed.set_footer(text="Son Güncelleme Tarihi: "+tarih)
			await message.send(embed=embed)
		else:
			kursunsuz = c.akaryakıt("K95") + " ₺ "
			dizel = c.akaryakıt("Mot50") + " ₺ "
			prodizel = c.akaryakıt("MotPro") + " ₺ "
			lpg = c.akaryakıt("PoGaz") + " ₺ "
		
		
			tarih = datetime.datetime.now()
			saat = tarih.hour
		
			tarih = str(saat) +"."+ str(tarih.minute) +"  "+ str(tarih.day) +"."+ str(tarih.month) +"."+ str(tarih.year)
		
			embed=discord.Embed(title = "İstanbul Avrupa Fiyatları Baz Alınmıştır" ,color=0x00ffff)
			embed.add_field(name="Kurşunsuz 95: ", value=kursunsuz, inline=False)
			embed.add_field(name="Diesel: ", value=dizel, inline=False)
			embed.add_field(name="Pro Diesel: ", value=prodizel, inline=False)
			embed.add_field(name="LPG: ", value=lpg, inline=False)
			embed.set_footer(text="Son Güncelleme Tarihi: "+tarih)
			await message.send(embed=embed)

	
def setup(bot):
		bot.add_cog(kurBilgisi(bot))
