import requests

import pandas as pd 

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids" : 'bitcoin',
    "vs_currencies": "usd"
}

r = requests.get(url, params = params )
data = r.json()
print(data)

df = pd.DataFrame(data)
print(df)


df.to_csv("crypto_price.csv", index=False)