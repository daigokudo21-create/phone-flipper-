from flask import Flask,render_template
from scraper_yahoo import get_yahoo_items
from damage_classifier import classify
from parts_db import get_part
from mercari_price import get_price
from profit_calc import calc

app = Flask(__name__)

def detect_model(title):

    title = title.lower()

    if "iphone13" in title:
        return "iphone13"

    if "iphone12" in title:
        return "iphone12"

    if "iphone11" in title:
        return "iphone11"

    return None


@app.route("/")
def home():

    auctions = get_yahoo_items()

    results = []

    for a in auctions:

        model = detect_model(a["title"])

        if not model:
            continue

        damage = classify(a["title"])

        if not damage:
            continue

        part = get_part(model,damage)

        if not part:
            continue

        mercari = get_price(model)

        if not mercari:
            continue

        profit = calc(a["price"],part,mercari)

        if profit > 0:

            results.append({
                "title":a["title"],
                "profit":profit,
                "url":a["url"]
            })

    results.sort(key=lambda x:x["profit"],reverse=True)

    return render_template("index.html",items=results)


app.run(host="0.0.0.0",port=10000)