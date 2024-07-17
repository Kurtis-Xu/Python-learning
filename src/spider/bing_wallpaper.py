import asyncio
import os

import aiofiles
import aiohttp
import requests
from lxml import etree

DOMAIN = 'https://bing.wdbyte.com'
SCAN_MONTH_TASKS = []
DOWNLOAD_TASKS = []

POOL = asyncio.Semaphore(10)

DIR = 'C:\\Users\\schuke\\Pictures\\bing'
if not os.path.exists(DIR): os.makedirs(DIR)

months = map(
    lambda m: m.xpath('./text()')[0],
    etree.HTML(requests.get(DOMAIN).text).xpath('/html/body/div/div[2]/div[2]/p/a')
)

async def download(info, m: str):
    filename = str(info.xpath('./text()')[0]).strip()
    m_dir = os.path.join(DIR, m)
    if not os.path.exists(m_dir): os.makedirs(m_dir)

    file = os.path.join(m_dir, f'{filename}.jpg')
    if os.path.exists(file): return
    img_url = info.xpath('./a/@href')[0]
    async with POOL:
        async with aiohttp.ClientSession() as session:
            async with session.get(img_url) as res:
                async with aiofiles.open(file, 'wb') as img:
                    await img.write(await res.content.read())
                    print(filename, '下载完成！')

async def scan_month(m: str):
    async with POOL:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{DOMAIN}/{m}') as res:
                image_infos = etree.HTML(await res.text()).xpath('/html/body/div/div[1]/div/p')
                for image_info in image_infos:
                    DOWNLOAD_TASKS.append(asyncio.create_task(download(image_info, m)))

async def main():
    for month in months:
        SCAN_MONTH_TASKS.append(asyncio.create_task(scan_month(month)))
    await asyncio.gather(*SCAN_MONTH_TASKS)
    await asyncio.gather(*DOWNLOAD_TASKS)

asyncio.run(main())
