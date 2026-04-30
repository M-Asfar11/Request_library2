import requests
import pandas as pd 


coins = ["bitcoin", "ethereum", "dogecoin", "bnb", "tron", "solana"]

def crypto_data(coin_list):
    url = "https://api.coingecko.com/api/v3/simple/price"    
    params = {
            'ids' : ','.join(coin_list),
            "vs_currencies": "usd"
        }

    try:
        r = requests.get(url, params=params)
        if r.status_code != 200:
            print("Error:", r.status_code)
            return None

        data = r.json()
        result = []

        for coin in coin_list:
            price = data.get(coin, {}).get("usd")
            result.append(
                {
                "coin": coin,
                "usd_price": price
                })

        return result

    except Exception as e:
        print(f"failed: {e}")
        return []

data_list = crypto_data(coins)
df = pd.DataFrame(data_list)
df.to_csv("mycrypto.csv")
print("Data saved to mycrypto.csv")
print(df)
