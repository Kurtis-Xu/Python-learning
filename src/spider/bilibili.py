import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome\
    /126.0.0.0 Safari/537.36',
}

res = requests.get("https://www.bilibili.com", headers=headers)

print(res.text)
