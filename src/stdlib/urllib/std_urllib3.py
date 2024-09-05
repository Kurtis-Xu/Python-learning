# urllib3.request.urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)
import urllib3

baidu = urllib3.PoolManager()
print('百度', baidu.request('GET', 'http://www.baidu.com').info())

google = urllib3.ProxyManager('http://127.0.0.1:81')  # 使用代理
print('谷歌', google.request('GET', 'http://www.google.com').info())
