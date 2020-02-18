def discounted(price, discount, max_discount=20, name=''):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError("Слишком большая скидка")
        if discount >= max_discount or "iphone" in name.lower() or not name:
            return price
        else:
            return price - (price*discount/100)
    except ValueError:
        return "Данные введены некорректно!"


def main():
    phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25}
    phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000, 'discount': 10}
    phone3 = {'name': 'iPhone 11', 'stock': 8, 'price': 100500, 'discount': 0}

    dis_iphone = discounted(phone1['price'], phone1['discount'], name=phone1['name'])
    dis_samsung = discounted(phone2['price'], phone2['discount'], name=phone2['name'])
    dis_noname = discounted(100, 10)
    dis_incorrect = discounted(phone3['price'], "Хочу чтобы бесплатно", name=phone3['name'])

    print(dis_iphone)
    print(dis_samsung)
    print(dis_noname)
    print(dis_incorrect)


if __name__ == '__main__':
    main()