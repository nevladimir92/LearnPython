def ask_user_dict():
    q_dict = {
        'что делаешь': 'Программирую.',
        'как дела': 'Отлично!'
        # ...
    }
    answer = input("Привет! Как дела? \n").lower()
    while True:
        if answer == "пока":
            print("Ну пока!")
            break

        answer = input("Давай спрашивай что хотел... \n")
        answer = answer.lower().strip("?.")
        if answer in q_dict:
            print(q_dict[answer])
        else:
            print("Не то спрашиваешь. Сформулируй и давай еще раз")


if __name__ == '__main__':
    ask_user_dict()