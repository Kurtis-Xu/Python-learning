import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                  '/126.0.0.0 Safari/537.36',
}

for start_num in range(0, 250, 25):
    res = requests.get(f'https://movie.douban.com/top250?start={start_num}', headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.findAll('span', attrs={'class': 'title'})
    for title in titles:
        if '/' not in str(title.string):
            print(title.string)
