import requests
from bs4 import BeautifulSoup

url = 'http://www.xinfadi.com.cn/index.html'
res = requests.get(url)

page = BeautifulSoup(res.text, 'html.parser')

table = page.find('div', id='div').find('table')

print(table)
