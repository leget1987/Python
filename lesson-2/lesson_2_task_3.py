#user_month = int(input("Введите месяц по счету, а я сообщу какое это время года: "))
user_month = 9
season = ["Зима", "Весна", "Лето", "Осень"]


if user_month == 1 or user_month == 2 or user_month == 12:
    print(f'Время года {(season[0])}')
elif user_month == 5 or user_month == 4 or user_month == 3:
    print(f'Время года {(season[1])}')
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(f'Время года {(season[2])}')
elif user_month == 9 or user_month == 10 or user_month == 11:
    print(f'Время года {(season[3])}')

dict_season = {
    1: "Зима",
    2: "Зима",
    12: "Зима",
    3: "Весна",
    4: "Весна",
    5: "Весна",
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень",
}
print(f"Время года - {dict_season.get(user_month)}")