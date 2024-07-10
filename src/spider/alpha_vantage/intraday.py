import requests

res = requests.get(
    "https://www.alphavantage.co/query", params=dict(
        function='TIME_SERIES_INTRADAY',
        symbol='COMP',
        interval='1min',
        outputsize='compact',
        apikey='UMW2GZUN5M5WBQUH'
    )
)

print(res.text)
