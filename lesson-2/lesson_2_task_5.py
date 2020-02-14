rating = [7, 5, 3, 2]
#user_rating = int(input('Введите свой рейтинг - натуральное число: '))
user_rating = 4
rating.append(user_rating)
rating.sort(reverse=True)
print(rating)
