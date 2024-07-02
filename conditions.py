def get_positive_count():
    numbers_count = 0
    try:
        if int(input("Введите первое число: ")) > 0:
            numbers_count += 1
        if int(input("Введите второе число: ")) > 0:
            numbers_count += 1
        if int(input("Введите третье число: ")) > 0:
            numbers_count += 1
    except ValueError:
        print("Ошибка ввода!")
    else:
        print(f"Количество положительных чисел: {numbers_count}")


def get_max_number():
    try:
        first_number = float(input("Введите первое число: "))
        second_number = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка ввода!")
    else:
        if first_number == second_number:
            pass
        elif first_number > second_number:
            print(f"Большее число: {first_number}")
        else:
            print(f"Большее число: {second_number}")


def get_min_max_number():
    try:
        first_number = float(input("Введите первое число: "))
        second_number = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка ввода!")
    else:
        if first_number == second_number:
            pass
        elif first_number > second_number:
            print(f"Большее число: {first_number}")
            print(f"Меньшее число: {second_number}")
        else:
            print(f"Большее число: {second_number}")
            print(f"Меньшее число: {first_number}")


def get_min_number():
    try:
        first_number = float(input("Введите первое число: "))
        second_number = float(input("Введите второе число: "))
        third_number = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка ввода!")
    else:
        if not first_number == second_number == third_number:
            if first_number > second_number:
                min_number = second_number
            else:
                min_number = first_number
            if min_number > third_number:
                min_number = third_number
            print(f"Минимальное из чисел: {min_number}")


def get_quarter_number():
    quarter_number = 0
    try:
        x = float(input("Введите координату X: "))
        y = float(input("Введите координату Y: "))
    except ValueError:
        print("Ошибка ввода!")
    else:
        if x != 0 and y != 0:
            if y > 0:
                if x > 0:
                    quarter_number = 1
                else:
                    quarter_number = 4
            else:
                if x > 0:
                    quarter_number = 2
                else:
                    quarter_number = 3
            print(f"Точка принадлежит {quarter_number}-ой четверти")
        else:
            print("Точка принадлежит оси координат ")



if __name__ == '__main__':
    # get_positive_count()
    # get_max_number()
    # get_min_max_number()
    # get_min_number()
    # get_quarter_number()
    pass