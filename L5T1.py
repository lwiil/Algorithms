# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


from collections import defaultdict, OrderedDict


d = defaultdict(list)
total = defaultdict(list)
avg_amount = 0
a = int(input('Введите количество компаний:\n'))
for i in range(a):
    name = input('Введите имя {} компании:\n'.format(i+1))
    d[name].append(list(int(i) for i in input('Введите прибыль за каждый квартал для компании {} (4 числа) через пробел:\n'.format(name)).split()))

# средняя сумма прибыли за год для одной компании
for name, value in d.items():
    for i in value:
        total[name].append((sum(i)/4.0))
print(total)


# находим среднюю прибыль за год для всех компаний
for value in total.values():
    avg_amount = avg_amount + value[0]
print('Средняя прибыль за год составляет {}'.format(avg_amount/a))


for i, v in total.items():
    if float(v[0]) < (avg_amount/a):
        print('У компании {} прибыль ниже среднего'.format(i))
    else:
        continue
