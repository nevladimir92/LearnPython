def define_work(age):
    age = int(age)
    if age < 2:
        print("Не учится и не работает")
    elif 2 < age < 6:
        print("Учится в детском саду")
    elif age < 17:
        print("Учится в школе")
    elif age < 22:
        print("Учится в ВУЗе")
    elif age < 60:
        print("Работает")
    else:
        print("Пенсионер")


def occupation(age):
    age = int(age)
    some_dict = [
        {"Не учится и не работает" : [0, 2]},
        {"Учится в детском саду": [2, 7]},
        {"Учится в школе" : [7, 18]},
        {"Учится в ВУЗе" : [18, 23]},
        {"Работает" : [23, 61]},
        {"Пенсионер" : [60, 222]}
    ]

    for i in some_dict:
        for key, value in i.items():
            if age in range(value[0], value[1]):
                print(key)
            else:
                continue


def main():
    age = input("Пожалуйста, введите Ваш возраст: ")
    define_work(age)
    age1 = input("Пожалуйста, введите Ваш возраст: ")
    occupation(age1)


if __name__ == "__main__":
    main()