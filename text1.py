import requests
from bs4 import BeautifulSoup
import time 

stock=["1101","5347"]

for i in range(len(stock)):
  stockid=stock[i]
  url = "https://tw.stock.yahoo.com/quote/"+ stockid +".TW"
  r = requests.get(url)
  soup = BeautifulSoup(r.text,'html.parser')
  price = soup.find('span',class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'])
  if price == None:
    url = "https://tw.stock.yahoo.com/quote/"+ stockid +".TWO"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    price = soup.find('span',class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'])

  meg= "股票" + stockid + "的即時價格為:" + price.getText()
  token = '6420496655:AAFNmGxfTU_r8GjLrEp8xygQUTBb39YaBNk'
    # 使用者 id
  chat_id="1722040126"
  # bot 送訊息
  url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={meg}"
  requests.get(url)
  time.sleep(3)



