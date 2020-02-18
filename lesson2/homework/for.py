from statistics import mean


def school_marks(marks):
    mean_marks = []
    for class_info in marks:
        mean_marks.append(mean(class_info['scores']))

    return "Средняя оценка по школе {:.1f}".format(mean(mean_marks))

    # или
    # for class_info in marks:
    #     scores = class_info['scores']
    #     mean_marks.append(sum(scores)/len(scores))
    #
    # return "{:.1f}".format(sum(mean_marks)/len(mean_marks))


def class_marks(marks):
    to_print = []
    for item in marks:
        to_print.append("Средняя оценка класса {} -> {:.1f}".format(item['school_class'], mean(item['scores'])))

        # или без return
        # print("Средняя оценка класса {} -> {:.1f}".format(item['school_class'], mean(item['scores'])))

    return "\n".join(to_print)


def main():
    marks = [
        {'school_class': '4a', 'scores': [3, 4, 5, 5, 2, 2]},
        {'school_class': '4b', 'scores': [1, 2, 5, 4]},
        {'school_class': '4c', 'scores': [5, 5, 5, 5, 4]},
        {'school_class': '5a', 'scores': [3, 4, 4, 3, 3, 3, 3]},
        {'school_class': '5b', 'scores': [1, 1, 1, 1, 1, 1, 5]},
        {'school_class': '5c', 'scores': [2, 5, 5, 5, 5, 2]}
    ]

    print(school_marks(marks))
    print(class_marks(marks))


if __name__ == '__main__':
    main()
