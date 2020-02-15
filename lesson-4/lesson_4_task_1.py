# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

if len(argv) == 4:
    print(f'Ваша зарплата - {float(argv[1]) * float(argv[2]) + float(argv[3])}')
elif len(argv) == 3:
    print(f'Ваша зарплата - {float(argv[1]) * float(argv[2])}')
else:
        print("Вы ввели слишком мало параметров, введите количество отработанных часов, "
              "затем стоимость часа работы и вашу премию")
        earned_hours = float(input('Сколько часов вы отработали? '))
        rate_peer_hour = float(input('Какая у вас ставка в час? '))
        try:
            prize = float(input('Какая у вас премия? '))
            print(f'Вы заработали - {earned_hours * rate_peer_hour + prize}')
        except ValueError:
            print(f'Вы заработали - {earned_hours * rate_peer_hour}')
