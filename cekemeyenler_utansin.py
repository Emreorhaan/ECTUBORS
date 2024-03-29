import requests
import json
from bs4 import BeautifulSoup
from requests.api import request

_doviz_url = "http://bigpara.hurriyet.com.tr/doviz/"
_altin_url = "http://bigpara.hurriyet.com.tr/altin/"
_hisse_url = "https://bigpara.hurriyet.com.tr/borsa/hisse-senetleri/"
_petrol_url = "https://bigpara.hurriyet.com.tr/kobi/dunya-emtia-borsalari/brent-petrol/"

_r = requests.get(_doviz_url)
_soup = BeautifulSoup(_r.content,"html.parser")
	
_r2 = requests.get(_altin_url)
_soup2 = BeautifulSoup(_r2.content,"html.parser")
    
_r3 = requests.get(_hisse_url)
_soup3 = BeautifulSoup(_r3.content,"html.parser")

_r4 = requests.get(_petrol_url)
_soup4 = BeautifulSoup(_r4.content,"html.parser")
	
_doviz_verisi = _soup.find_all("div",{"class":"tableBox srbstPysDvz"})
	
_altin_verisi = _soup2.find_all("div",{"class":"table wide pgAltin"})

_hisse_verisi = _soup3.find_all("div", {"class":"contentLeft"})

_petrol_verisi = _soup4.find_all("div",{"class":"tableCnt"})

for _hisse in _hisse_verisi:
        
    _hisse_verileri = _hisse.find_all("li")
	
for _doviz in _doviz_verisi:
        
    _doviz_verileri = _doviz.find_all("li")
	
for _altin in _altin_verisi:
        
    _altin_verileri = _altin.find_all("li")

for _petrol in _petrol_verisi:
        
    _petrol_verileri = _petrol.find_all("li")

def coin(_a):
    _coin_url = requests.get('https://api.binance.com/api/v3/ticker/price')
    _coinler = json.loads(_coin_url.content)
    _coin_fiyatlari = 0
    _coin_adi = _a

    for _coin in _coinler:
        if _coin['symbol'] == _coin_adi:
            _coin_fiyatlari = _coin['price']
            a = (_coin['price'])
            return a
def akaryakıt(_b):
    _akaryakıt_url = requests.get('https://www.petrolofisi.com.tr/posvc/fiyat/guncel?il=%C4%B0stanbul&Ilce=BAGCILAR')
    _akaryakıtlar = json.loads(_akaryakıt_url.content)
    for _akaryakıt in _akaryakıtlar:
        a = (_akaryakıt[_b])
        return a

def akaryakıt_il(_c):
    _akaryakıt_il_url = requests.get('https://www.petrolofisi.com.tr/posvc/fiyat/guncel')
    _akaryakıtlar = json.loads(_akaryakıt_il_url.content)
    _akaryakıt_il = _c

    for _akaryakıt in _akaryakıtlar:
        if _akaryakıt['Il'] == _akaryakıt_il:
            a = _akaryakıt
            return a
 
def dolar():
    _dolar = []
    _dolar.append((_doviz_verileri[6].text).strip())
    _dolar.append((_doviz_verileri[8].text).strip())
    _dolar.append((_doviz_verileri[9].text).strip())
    _dolar.append(((_doviz_verileri[10].text).strip())[:(len(_doviz_verileri[10].text) - 1)])
    return _dolar

def euro():
    _euro = []
    _euro.append((_doviz_verileri[12].text).strip())
    _euro.append((_doviz_verileri[14].text).strip())
    _euro.append((_doviz_verileri[15].text).strip())
    _euro.append(((_doviz_verileri[16].text).strip())[:(len(_doviz_verileri[16].text) - 1)])
    return _euro

def altin():
    _altin = []
    _altin.append((_altin_verileri[5].text).strip())
    _altin.append((_altin_verileri[6].text).strip())
    _altin.append((_altin_verileri[7].text).strip())
    _altin.append(((_altin_verileri[8].text).strip())[:(len(_doviz_verileri[8].text) - 1)])
    return _altin

def hisse():
    _hisse = []
    _hisse.append((_hisse_verileri[11].text).strip())
    _hisse.append((_hisse_verileri[12].text).strip())
    return _hisse

def petrol():
    _petrol = []
    _petrol.append((_petrol_verileri[7].text).strip())
    _petrol.append((_petrol_verileri[10].text).strip())
    return _petrol