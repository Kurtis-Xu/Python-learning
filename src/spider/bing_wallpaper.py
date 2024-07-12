import bs4
import requests

domain = 'https://bing.wdbyte.com'

months = bs4.BeautifulSoup(requests.get(domain).text, 'html.parser') \
    .find('div', class_='w3-margin') \
    .find_all('a')

for month in months:
    image_infos = bs4.BeautifulSoup(requests.get('/'.join([domain, month.get('href')])).text, 'html.parser') \
        .find('div', class_='w3-row-padding w3-padding-16 w3-center') \
        .find_all('p')

    for image_info in image_infos:
        image_name = str(image_info.get_text()).split(' ')[0]
        image_url = image_info.find('a').get('href')
        with open(f'C:\\Users\\schuke\\Pictures\\bing\\{image_name}.jpg', 'wb') as img:
            img.write(requests.get(image_url).content)
