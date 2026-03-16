import requests
from bs4 import BeautifulSoup

def get_yahoo_items():

    url = "https://auctions.yahoo.co.jp/search/search?p=iphone+ジャンク"

    r = requests.get(url)

    soup = BeautifulSoup(r.text,"html.parser")

    items = []

    listings = soup.select(".Product")

    for l in listings:

        title = l.select_one(".Product__title")
        price = l.select_one(".Product__priceValue")
        link = l.select_one("a")

        if not title or not price:
            continue

        title = title.text.strip()
        price = int(price.text.replace("円","").replace(",",""))

        url = "https://auctions.yahoo.co.jp"+link["href"]

        items.append({
            "title":title,
            "price":price,
            "url":url
        })

    return items