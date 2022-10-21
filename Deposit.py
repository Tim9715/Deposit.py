money = int(input('Введите сумму: '))
time = 365
time2 = 365
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a1 = (money * per_cent['ТКБ'] * time / time2) / 100
a2 = (money * per_cent['СКБ'] * time / time2) / 100
a3 = (money * per_cent['ВТБ'] * time / time2) / 100
a4 = (money * per_cent['СБЕР'] * time / time2) / 100
b = [int(a1), int(a2), int(a3), int(a4)]
print('Cуммы, которые вы можете заработать — ', end='')
print(*b, sep=', ')
print('Максимальная сумма, которую вы можете заработать —', max(b))