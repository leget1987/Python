# Простое решение с помощью **
exponentiation = lambda x, y: x ** y

print(exponentiation(2, -5))


# Решение без **
def exponentiation_3(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return 1
    elif y == 1:
        return x
    elif y < 0:
        positive_number_y = abs(y)
        z = x
        while positive_number_y > 1:
            z *= x
            positive_number_y -= 1
        return 1 / z
    else:
        z = x
        while y > 1:
            z *= x
            y -= 1
        return z


print(exponentiation_3(2, -5))


# Решение с помощью рекурсии
def exponentiation_2(x, y):
    if x == 0:
        return 0
    elif y == 0:
        return 1
    elif y == 1:
        return x
    elif y < 0:
        return 1 / (x * exponentiation_2(x, -y - 1))
    else:
        return x * exponentiation_2(x, y - 1)


print(exponentiation_2(2, -5))
