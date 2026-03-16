def calc(buy,part,mercari):

    sell = mercari * 0.9

    fee = sell * 0.10

    shipping = 300

    profit = sell - fee - shipping - buy - part

    return int(profit)