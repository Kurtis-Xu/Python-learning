import os
from concurrent.futures import ThreadPoolExecutor

import requests
from lxml import etree

DOMAIN = 'https://bing.wdbyte.com'

DIR = 'C:\\Users\\schuke\\Pictures\\bing'
if not os.path.exists(DIR): os.makedirs(DIR)

months = map(
    lambda m: m.xpath('./text()')[0],
    etree.HTML(requests.get(DOMAIN).text).xpath('/html/body/div/div[2]/div[2]/p/a')
)

def download(info):
    filename = str(info.xpath('./text()')[0]).strip()
    with open(f'{DIR}\\{filename}.jpg', 'wb') as img:
        img_url = info.xpath('./a/@href')[0]
        img.write(requests.get(img_url).content)
        print(img_url, '下载完成！')

with ThreadPoolExecutor(100) as exe:
    for month in months:
        image_infos = etree.HTML(requests.get(f'{DOMAIN}/{month}').text).xpath('/html/body/div/div[1]/div/p')
        for image_info in image_infos:
            exe.submit(download, image_info)
