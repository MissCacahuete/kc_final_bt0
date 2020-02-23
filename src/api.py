import requests

from src.api_domain.price_conversion import PriceConversion
from src.domain.crypto import Crypto

base_path= "https://pro-api.coinmarketcap.com"
api_key= 'APY_KEY' #api key real
api_key_param="CMC_PRO_API_KEY="
symbol_param="symbol="
amount_param= "amount="
convert_param="convert="
g_coins= "/v1/cryptocurrency/map?{}{}&{}BTC,ETH,XRP,LTC,BCH,BNB,USDT,EOS,BSV,XLM,ADA,TRX".format(api_key_param, api_key, symbol_param)
c_coins= "/v1/tools/price-conversion?{}{}".format(api_key_param, api_key)

def get_coins():
    api_response= requests.get("{}{}".format(base_path, g_coins))
    data=api_response.json()["data"]
    cryptonedas = []
    for currency in data:
        c=Crypto(currency["id"],currency["name"],currency["symbol"])
        cryptonedas.append(c)
    return cryptonedas

def convert_coins(quantity, from_currency, to_currency):
    print(f"Convert {quantity} from {from_currency} to {to_currency}")
    api_response= requests.get("{}{}&{}{}&{}{}&{}{}".format(base_path, c_coins, amount_param, quantity, symbol_param, from_currency, convert_param, to_currency))
    print(api_response.json())
    data=api_response.json()["data"]
    m=PriceConversion(data["id"],data["symbol"],data["name"],data["amount"],data["last_updated"],to_currency,data["quote"][to_currency]["price"])
    return m

if __name__ == "__main__":
    pass