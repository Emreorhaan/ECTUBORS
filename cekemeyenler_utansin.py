import requests
import json
from bs4 import BeautifulSoup
from requests.api import request

_doviz_url = "http://bigpara.hurriyet.com.tr/doviz/"
_altin_url = "http://bigpara.hurriyet.com.tr/altin/"
_hisse_url = "https://bigpara.hurriyet.com.tr/borsa/hisse-senetleri/"
_petrol_url = "https://bigpara.hurriyet.com.tr/kobi/dunya-emtia-borsalari/brent-petrol/"
_akaryakıt_url = "https://www.petrolofisi.com.tr/akaryakit-fiyatlari"

_r = requests.get(_doviz_url)
_soup = BeautifulSoup(_r.content,"html.parser")
	
_r2 = requests.get(_altin_url)
_soup2 = BeautifulSoup(_r2.content,"html.parser")
    
_r3 = requests.get(_hisse_url)
_soup3 = BeautifulSoup(_r3.content,"html.parser")

_r4 = requests.get(_petrol_url)
_soup4 = BeautifulSoup(_r4.content,"html.parser")

_r5 = requests.get(_akaryakıt_url)
_soup5 = BeautifulSoup(_r5.content,"html.parser")
	
_doviz_verisi = _soup.find_all("div",{"class":"tableBox srbstPysDvz"})
	
_altin_verisi = _soup2.find_all("div",{"class":"table wide pgAltin"})

_hisse_verisi = _soup3.find_all("div", {"class":"contentLeft"})

_petrol_verisi = _soup4.find_all("div",{"class":"tableCnt"})

_akaryakıt_verisi = _soup5.find_all("div",{"class":"current-price-result-container current-price-result-container--secondary"})

for _hisse in _hisse_verisi:
        
    _hisse_verileri = _hisse.find_all("li")
	
for _doviz in _doviz_verisi:
        
    _doviz_verileri = _doviz.find_all("li")
	
for _altin in _altin_verisi:
        
    _altin_verileri = _altin.find_all("li")

for _petrol in _petrol_verisi:
        
    _petrol_verileri = _petrol.find_all("li")
    
for _akaryakıt in _akaryakıt_verisi:
        
    _akaryakıt_verileri = _akaryakıt.find_all("td")

def coin(_b):
    _coin_url = requests.get('https://api.binance.com/api/v3/ticker/price')
    _coinler = json.loads(_coin_url.content)
    _coin_fiyatlari = 0
    _coin_adi = _b

    for _coin in _coinler:
        if _coin['symbol'] == _coin_adi:
            _coin_fiyatlari = _coin['price']
            a = (_coin['price'])
            return a
 
def dolar(self):
    _dolar = []
    _dolar.append((_doviz_verileri[6].text).strip())
    _dolar.append((_doviz_verileri[8].text).strip())
    _dolar.append((_doviz_verileri[9].text).strip())
    _dolar.append(((_doviz_verileri[10].text).strip())[:(len(_doviz_verileri[10].text) - 1)])
    return _dolar

def euro(self):
    _euro = []
    _euro.append((_doviz_verileri[12].text).strip())
    _euro.append((_doviz_verileri[14].text).strip())
    _euro.append((_doviz_verileri[15].text).strip())
    _euro.append(((_doviz_verileri[16].text).strip())[:(len(_doviz_verileri[16].text) - 1)])
    return _euro

def altin(self):
    _altin = []
    _altin.append((_altin_verileri[5].text).strip())
    _altin.append((_altin_verileri[6].text).strip())
    _altin.append((_altin_verileri[7].text).strip())
    _altin.append(((_altin_verileri[8].text).strip())[:(len(_doviz_verileri[8].text) - 1)])
    return _altin

def hisse(self):
    _hisse = []
    _hisse.append((_hisse_verileri[11].text).strip())
    _hisse.append((_hisse_verileri[12].text).strip())
    return _hisse

def petrol(self):
    _petrol = []
    _petrol.append((_petrol_verileri[7].text).strip())
    _petrol.append((_petrol_verileri[10].text).strip())
    return _petrol

def akaryakıt(self):
    _akaryakıt = []
    _akaryakıt.append((_akaryakıt_verileri[1].text).strip())
    _akaryakıt.append((_akaryakıt_verileri[2].text).strip())
    _akaryakıt.append((_akaryakıt_verileri[3].text).strip())
    _akaryakıt.append((_akaryakıt_verileri[4].text).strip())
    return _akaryakıt
