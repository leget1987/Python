def user_list(**kwargs):
    return kwargs


# Еще вариант с лямбда
user_list_2 = lambda **kwargs: kwargs

print(user_list(first_name='Дмитрий', last_name='Лобанов', birth_year=1987, city='Podolsk', email='leget@list.ru'))
print(user_list_2(first_name='Дмитрий', last_name='Лобанов', birth_year=1987, city='Podolsk', email='leget@list.ru'))
