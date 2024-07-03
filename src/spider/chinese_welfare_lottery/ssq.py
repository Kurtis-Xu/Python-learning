import csv
import json
import requests

url = 'https://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice'

params = dict(name='ssq', pageNo=1, pageSize=1, systemType='PC')

res = requests.get(url, params=params)

json_result = json.loads(res.text)['result']

if len(json_result) <= 0: raise Exception('没有获取到数据')

info_list = []
for item in json_result:
    arr = str(item['red']).split(',')
    info_list.append(
        [
            item['code'],
            int(arr[0]),
            int(arr[1]),
            int(arr[2]),
            int(arr[3]),
            int(arr[4]),
            int(arr[5]),
            int(item['blue'])
        ]
    )

info_list.reverse()

with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in info_list:
        writer.writerow(row)
