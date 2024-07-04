def get_point_description():
    try:
        point = int(input("Введите оценку от 1 до 5: "))
        if point > 5 or point < 1:
            raise ValueError
    except ValueError:
        print("Данные введены некорректно")
    else:
        match point:
            case 1:
                print("плохо")
            case 2:
                print("неудовлетворительно")
            case 3:
                print("удовлетворительно")
            case 4:
                print("хорошо")
            case 5:
                print("отлично")


def get_days_in_month():
    try:
        month_number = int(input("Введите номер месяца 1 до 12: "))
        if month_number > 12 or month_number < 1:
            raise ValueError
    except ValueError:
        print("Данные введены некорректно")
    else:
        match month_number:
            case 2:
                print("28 дней")
            case 4 | 6 | 9 | 11:
                print("30 дней")
            case _:
                print("31 день")


def match_next_day(day, month, last_day):
    if day > last_day:
        raise ValueError
    elif day == last_day:
        next_day = 1
        next_month = max((month + 1) % 13, 1)
    else:
        next_day = day + 1
        next_month = month
    return next_day, next_month


def get_next_day():
    try:
        month_number = int(input("Введите номер месяца 1 до 12: "))
        if month_number > 12 or month_number < 1:
            raise ValueError
        day = int(input("Введите число: "))

    except ValueError:
        print("Данные введены некорректно")
    else:
        match month_number:
            case 2:
                last_day = 28
            case 4 | 6 | 9 | 11:
                last_day = 30
            case _:
                last_day = 31

        print(match_next_day(day, month_number, last_day))


def numbers_to_string():
    first_part = ["", "cто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот",
                  "девятьсот"]
    second_part = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят",
                   "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    last_part = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять",
                 "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать",
                 "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    try:
        number = int(input("Введите трехзначное число: "))
        if number > 999 or number < 100:
            raise ValueError
    except ValueError:
        print("Данные введены некорректно")
    else:
        number_parts = [number // 100]
        tail_number = number % 100
        if tail_number > 19:
            number_parts.append(tail_number // 10)
            number_parts.append(tail_number % 10)
        else:
            number_parts.append(tail_number)
        match number_parts:
            case a, b:
                print(f"{first_part[a]} {last_part[b]}")
            case a, b, c:
                print(f"{first_part[a]} {second_part[b]} {last_part[c]}")


def simple_calculate():
    try:
        first_operand = float(input("Введите первый операнд: "))
        operation = str(input("введите операцию (+, -, *, /): "))
        if operation not in ("+", "-", "*", "/"):
            raise ValueError
        second_operand = float(input("Введите второй операнд: "))

    except ValueError:
        print("Данные введены некорректно")
    else:
        match operation:
            case "+":
                print(f"{first_operand} + {second_operand} = {first_operand + second_operand}")
            case "-":
                print(f"{first_operand} - {second_operand} = {first_operand - second_operand}")
            case "*":
                print(f"{first_operand} * {second_operand} = {first_operand * second_operand}")
            case "/":
                print(f"{first_operand} / {second_operand} = {first_operand / second_operand}")


def robot():
    directions = ('С', 'З', 'Ю', 'В')
    current_direction = 'С'
    for _ in range(10):
        action = input("Введите действие: ")
        match action:
            case "1":
                current_direction = directions[(directions.index(current_direction) + 1) % 4]
            case "-1":
                current_direction = directions[directions.index(current_direction) - 1]
        print(current_direction)


if __name__ == '__main__':
    # get_point_description()
    # get_days_in_month()
    # get_min_max_number()
    # get_min_number()
    # get_quarter_number()
    # get_next_day()
    # numbers_to_string()
    # simple_calculate()
    robot()
