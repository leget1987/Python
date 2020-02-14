#user_list = [input("Введите элементы списка через запятую: ")]
user_list = ['строка', 8, 8.3, True, None, {"age": 10, "name": "Leo"}, [], ()]
user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]
print(user_list)

