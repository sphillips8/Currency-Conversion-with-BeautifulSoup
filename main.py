from bs4 import BeautifulSoup
import requests

def convert_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = rate.split()[0]

  return in_currency, out_currency, float(rate)

in_currency, out_currency, rate = convert_currency(in_currency='EUR', out_currency='AUD')

if rate < 1:
  compare = 'less valuable than'
elif rate > 1:
  compare = 'more valuable than'
else: 
  compare = 'the same value as'

print(f' 1 {in_currency} = {rate} {out_currency} \n 1 {in_currency} is {compare} 1 {out_currency}')
  