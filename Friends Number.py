import redis
red = redis.Redis(host ='',
                  port = ,
                  password ='')
a = input('Введите задачу - Добавить, Удалить, Показать: ')
def add():
    return red.set(input('Введите имя друга: '), input('Введите номер друга: '))
def delete():
    return  red.delete(input('Введите имя друга: '))
def print1():
    return print(red.get(input('Введите имя друга: ')))
if a == 'Добавить':
    add()
elif a == 'Удалить':
    delete()
elif a == 'Показать':
    print1()
