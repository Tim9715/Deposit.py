sequence = [int(i) for i in input('Введите последовательность чисел, в диапазоне 0 - 1000 через пробел: ').split()]
def sort(sequence):
    for i in range(len(sequence)):
        for j in range(len(sequence) - i - 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
    return sequence
print('Последовательность отсортирована:', sort(sequence))
def binary_search(sequence, element):
    a = []
    if min(sequence) > element:
        return print('Такой элемент отсутствует')
    for index in range(len(sequence)):
        if element > sequence[index - 1] and element <= sequence[index + 1]: #Если число меньше введенного пользователем числа и если число больше ведённого пользователем числа
            a.append(index) #Закидываем в список два индекса числа меньше введённого и числа больше
    return a
while True:
    try:
        element = int(input("Введите число в диапазоне 0 - 1000: "))
        if 0 <= element <= 1000:
            break
        else:
            raise ValueError
    except ValueError:
        print("Вы ввели не число или число не входит в указанный диапазаон. Попробуйте снова: ")
print('Индексы элементов начиная с 0:', end=' ')
print(*binary_search(sequence, element), sep=', ')