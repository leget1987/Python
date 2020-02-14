goods_list = [
    (1, {'Наименование': 'компьютер', 'Цена': '10000', 'Количество': '3', 'ед': 'шт'}),
    (2, {'Наименование': 'ноутбук', 'Цена': '12000', 'Количество': '2', 'ед': 'шт'}),
    (3, {'Наименование': 'принтер', 'Цена': '4000', 'Количество': '5', 'ед': 'шт'})
]
# goods_list = []
# goods_tuple = []
# count_goods = int(input('Введите количество товаров, которые хотите внести в базу: '))
# goods = {
#     'Наименование': None,
#     'Цена': None,
#     'Количество': None,
#     'ед': None,
# }
# el = 0
# while el != count_goods:
#     for i in goods:
#         goods[i] = input(f'Введите {i}: ')
#     goods.copy()
#     goods_tuple.append(el + 1)
#     goods_tuple.append(goods.copy())
#     goods_list.append(tuple(goods_tuple.copy()))
#     goods_tuple.clear()
#     el += 1
#
# print(goods_list)


result = {}
for number, value in goods_list:
    for k, v in value.items():
        try:
            result[k] += [v]
        except:
            result[k] = [v]

# Убираю дублирование "шт"

result['ед'] = list(set(result.get('ед')))
print(result)