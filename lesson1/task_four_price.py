def format_price(price):

    price = int(price)
    result = f"Цена: {price} руб."
    return result


print(format_price(56.24))