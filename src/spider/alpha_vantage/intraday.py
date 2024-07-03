import requests

res = requests.get(
    "https://www.alphavantage.co/query", params=dict(
        function='TIME_SERIES_INTRADAY',
        symbol='1A001',
        interval='60min',
        apikey='UMW2GZUN5M5WBQUH'
    )
)

print(res.text)
