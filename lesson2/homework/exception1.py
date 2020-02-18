def ask_user():
    q_dict = {
        'что делаешь': 'Программирую.',
        'как дела': 'Отлично!',
        'что нового': 'Да все по старому...'
        # ...
    }
    while True:
        try:
            answer = input("Привет! Как дела? \n").lower()
            while True:
                answer = input("Давай спрашивай что хотел... \n")
                answer = answer.lower().strip("?.")
                if answer == "пока":
                    print("Ну пока!")
                    break
                if answer in q_dict:
                    print(q_dict[answer])
                else:
                    print("Не то спрашиваешь. Сформулируй и давай еще раз")
        except KeyboardInterrupt:
            print("Давай, пока!")
            break


if __name__ == "__main__":
    ask_user()
