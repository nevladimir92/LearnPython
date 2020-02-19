def find_user(name):
    names = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

    while True:
        curr_name = names[0]
        if name == curr_name:
            print(f"{name} нашелся(нашлась)")
            break
        else:
            names.pop(0)


if __name__ == '__main__':
    find_user("Маша")