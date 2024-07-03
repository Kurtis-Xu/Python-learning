import requests

res = requests.get(
    "https://www.alphavantage.co/query", params=dict(
        function='SYMBOL_SEARCH',
        keywords='中',
        apikey='UMW2GZUN5M5WBQUH'
    )
)

print(res.text)
