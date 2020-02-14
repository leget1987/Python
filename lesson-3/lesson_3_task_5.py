stop = None
summa = 0
while True:
    user_number = input("Введите числа через пробел, я посчитаю их сумму. Для выхода введите 'q': ")
    number = user_number.split(' ')
    list_number = []
    try:
        for i in range(len(number)):
            if number[i] != 'q':
                list_number.append(float(number[i]))
            elif number[i] == 'q':
                stop = 1
                summa += sum(list_number)
    except:
        print('Вводите значения через 1 пробел')
        continue
    if stop:
        print(f'Сумма введеных чисел равна {summa}')
        print('Вы вышли из программы')
        break
    summa += sum(list_number)
    print(summa)
