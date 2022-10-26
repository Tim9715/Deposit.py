tickets = int(input('Введите количество билетов: '))
age = [int(input('Введите возраст покупателя: ')) for i in range(1, tickets + 1)]
stoimost = 0
FinallStoimost = 0
for i in age:
    if i < 18:
        stoimost += 0
    elif i >= 18 and i <= 25:
        stoimost += 990
    elif i >= 25:
        stoimost += 1390
if tickets > 3:
    FinallStoimost = stoimost - (stoimost / 100 * 10)
    print(int(FinallStoimost))
else:
    print(stoimost)