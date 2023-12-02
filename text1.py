import requests
from bs4 import BeautifulSoup
import time

stock = ["1101","2330"]

for i in range(len(stock)):
  stockid = stock[i]
  url = 'https://tw.stock.yahoo.com/quote/'+ stockid +'.TW'
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  price = soup.find('span', class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)']).getText()
  print(price)

  if price == none:
    url = 'https://tw.stock.yahoo.com/quote/'+ stockid +'.TWO'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('span', class_=['Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)','Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)']).getText()
    price = price.getText()
message = "股票"+stockid+" 即時股價為: "+ price
token = '6420496655:AAFNmGxfTU_r8GjLrEp8xygQUTBb39YaBNk'
chat_id="輸入你的 telegram id"
url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
requests.get(url)
time.sleep(3)



