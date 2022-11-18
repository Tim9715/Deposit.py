class client:
    def __init__(self, name, surname, place, balance):
        self.name = name
        self.surname = surname
        self.place = place
        self.balance = balance
    def __str__(self):
        return f'{self.name} {self.surname}. {self.place}. Баланс:{self.balance} руб.'
    def get_guest(self):
        return f'{self.name} {self.surname}. {self.place}'
a = client('Иван', 'Петров', 'Москва', 50)
b = client('Владимир','Зайцев','Кострома',50)
c = client('Олеся','Янина','Новосибирск',50)
s = [a, b, c]
print(*s, sep='\n')
for i in s:
    print(i.get_guest())
