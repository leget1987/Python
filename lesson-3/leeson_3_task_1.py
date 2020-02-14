def division(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        return ('Деление на 0 запрещено')


# num_1 = int(input('Введите первое число, которое хотите разделить: '))
# num_2 = int(input('Введите второе число, на которое хотите разделить: '))

num_1 = 50
num_2 = 20
print(division(num_1, num_2))
