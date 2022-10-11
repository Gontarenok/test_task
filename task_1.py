def check_relation(net, first, second):
    pair = []

    for i in net:
        if first in i or second in i:
            pair.append(i)

    return pair


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"),
        ("Лёша", "Катя"),
        ("Ваня", "Катя"),
        ("Вова", "Катя"),
        ("Лёша", "Лена"),
        ("Оля", "Петя"),
        ("Стёпа", "Оля"),
        ("Оля", "Настя"),
        ("Настя", "Дима"),
        ("Дима", "Маша")
    )

    res = check_relation(net, "Петя", "Стёпа")
    print(res)

    # assert check_relation(net, "Петя", "Стёпа") is True
    # assert check_relation(net, "Маша", "Петя") is True
    # assert check_relation(net, "Ваня", "Дима") is False
    # assert check_relation(net, "Лёша", "Настя") is False
    # assert check_relation(net, "Стёпа", "Маша") is True
    # assert check_relation(net, "Лена", "Маша") is False
    # assert check_relation(net, "Вова", "Лена") is True
