def get_summ(first, second, delimiter="&"):
    to_string = []
    first = str(first)
    second = str(second)
    to_string.append(first)
    to_string.append(second)
    string = delimiter.join(to_string)
    return string.upper()

def get_summ1(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    string = one + delimiter + two
    return string.upper()

print(get_summ("Learn", "Python"))
print(get_summ1("Learn", "Python"))