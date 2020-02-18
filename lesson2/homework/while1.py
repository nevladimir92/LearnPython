def ask_user():
    while True:
        answer = input("Как дела? \n").lower()
        if answer == "хорошо":
            print("Ну и хорошо!")
            break


if __name__ == '__main__':
    ask_user()