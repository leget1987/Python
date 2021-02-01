def sum_arg(num_1, num_2, num_3):
    return sum([num_1, num_2, num_3]) - min(num_1, num_2, num_3)


# Вариант с лямбда функцией
arg_sum = lambda x, y, z: sum([x, y, z]) - min(x, y, z)

print(arg_sum(500, 80, 100))
print(sum_arg(500, 80, 100))
