import requests

res = requests.get('http://www.baidu.com')

with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(res.content.decode('utf-8'))
    f.close()
print('over!')
