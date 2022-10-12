''' Дан массив связей пользователей. Вам необходимо реализовать функцию,
которая принимает на вход три аргумента: информация о связях, как кортеж (tuple)
кортежей, первое имя (str), второе имя (str). Функция должна возвращать True, если
связь между любыми двумя заданными пользователями существует, например, если у
двух пользователей есть общие друзья или у их друзей есть общие друзья и т.д., иначе
False. '''



def check_relation(net, first, second, *args):

    # Получаем список переданных пользователей для рекурсии в дальнейшем
    all_user = [first, second]
    for i in args:
        all_user.append(i)

    print(f'users {all_user}')

    # Получаем список пар, где есть пользователи
    pair = []
    for i in net:
        for j in all_user:
            if j in i:
                pair.append(i)

    # print(f'users pair {pair}')

    # Делаем из списка пар общий список пользователей и их друзей
    pair_friends = []
    for i in pair:
        for j in i:
            pair_friends.append(j)

    # print(f'all list {pair_friends}')

    # Убираем первоначальных пользователей, оставляет только общих друзей
    mutual_friends = []
    for i in pair_friends:
        if i not in all_user:
            mutual_friends.append(i)

    print('mutual friends', mutual_friends)

    # Проверка на отсутствие общих друзей
    if len(mutual_friends) == 0:
        print(f'Пользователи не имеют общих связей.')
        return False

    # Делаем из списка множество - удаляем повторения. Если они были, значит были одинаковые общие друзья,
    # иначе используем рекурсию, чтобы проверить общих друзей на их общих друзей.

    set_mutual_friends = set(mutual_friends.copy())
    print('set', set_mutual_friends)

    if len(mutual_friends) > len(set_mutual_friends):
        print(f'Пользователи имеют общие связи.')
        return True
    else:
        try:
            # Передаем первоначальных пользователей в рекурсию, для того чтобы убрать их в начале
            # следующего выполнения функции, а также передаем их общих друзей, чтобы найти общих друзей у них
            check_relation(net, *all_user, *mutual_friends)
        except:
            print(f'Пользователи не имеют общих связей.')
            return False


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


    check_relation(net, "Петя", "Стёпа")
    check_relation(net, "Маша", "Петя")
    check_relation(net, "Ваня", "Дима")
    check_relation(net, "Лёша", "Настя")
    check_relation(net, "Стёпа", "Маша")
    check_relation(net, "Лена", "Маша")
    check_relation(net, "Вова", "Лена")

    # assert check_relation(net, "Петя", "Стёпа") is True
    # assert check_relation(net, "Маша", "Петя") is True
    # assert check_relation(net, "Ваня", "Дима") is False
    # assert check_relation(net, "Лёша", "Настя") is False
    # assert check_relation(net, "Стёпа", "Маша") is True
    # assert check_relation(net, "Лена", "Маша") is False
    # assert check_relation(net, "Вова", "Лена") is True
