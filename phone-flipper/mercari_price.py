import requests

def get_price(model):

    url=f"https://api.mercari.com/items/search?keyword={model}"

    r=requests.get(url)

    data=r.json()

    prices=[]

    for item in data["data"]:
        prices.append(item["price"])

    if not prices:
        return None

    avg=sum(prices)/len(prices)

    return avg