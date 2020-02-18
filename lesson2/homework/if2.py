def compare(str1, str2):
    if not (isinstance(str1, str) and isinstance(str2, str)):
        return 0

    str1 = str1.strip().lower()
    str2 = str2.strip().lower()

    if str1 == str2:
        return 1
    elif str1 != str2 and str2 == "learn":
        return 3
    elif len(str1) > len(str2):
        return 2
    else:
        return "Такого в условии нет, но пусть будет 4"


def main():
    print(compare('somestring', 'learn'))
    print(compare('somestring', 'python'))
    print(compare('learn', 'learn'))
    print(compare( 1, 'learn'))
    print(compare('estring', 'learnPython'))


if __name__ == "__main__":
    main()