# Второе задание первого урока
# time_user = int(input("Введите время в секундах, я ее переведу \
# его в формат чч.мм.сс: "))
time_user = 21010
time_hour = time_user // 3600
time_min = (time_user % 3600) // 60
time_sec = (time_user % 3600) % 60

print(f'Ваше время в формате чч.мм.сс: {time_hour}:{time_min}:{time_sec}')

# Третье задание первого урока
# number = input('Введите число n, а я посчитаю сумму в виде n + nn + nnn:')
number = "5"
print(int(number) + int(number + number) + int(number + number + number))

# Четвертое задание первого урока
# number = int(input("Введите целое положительное число: "))

number = 57885499
# Получаем последнюю цифру путем остатка от деления на 10
last_number = number % 10
# Целочисленным делением на 10 откидываем последнюю цифру
first_number = number // 10
while first_number > 0:
    if first_number % 10 > last_number:
        last_number = first_number % 10
    first_number = first_number // 10
print(last_number)

# Пятое задание первого урока
# revenue = int(input("Введите вашу выручку: "))
revenue = 100000
# cost = int(input("Введите ваши издержки: "))
cost = 60000
if revenue > cost:
    print("Вы работаете с прибылью")
    print("Рентабильность вашей выручки - ", \
          (revenue - cost) / revenue * 100, "%")
else:
    print("Ваша фирма убыточна")
# number_of_workers = int(input("Введите колт=ичество сотрудников "))
number_of_workers = 50
if revenue > cost:
    print('Прибыль фирмы в расчете на 1 сотрудника = ', \
          (revenue - cost) / number_of_workers)

# Шестое задание первого урока
a = 2
b = 3
day = 0
while a < b:
    day += 1
    print('В ', day, "- й день: ", a)
    a = a + (a * 0.1)
print('В ', day + 1, "- й день: ", a)
print('Ответ: на 6-й день спортсмен достиг результата - не менее 3 км')


