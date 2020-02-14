#user_in = input('Введите произвольную строку: ')
user_in = 'мама мыла раму средствомдлямытья'
user_list = user_in.split()
for idx, el in enumerate(user_list, 1):
    el = el[:10]
    print(idx, el)
