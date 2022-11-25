class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def left1(self, value2):
        if self.left is None:
            self.left = Tree(value2)
        else:
            child = Tree(value2)
            child.left = self.left
            self.left = child
        return  self
    def right1(self, value2):
        if self.right is None:
            self.right = Tree(value2)
        else:
            child = Tree(value2)
            child.right = self.right
            self.right = child
        return self
    def pre(self): #Префиксный подход
        print(self.value)
        if self.left is not None:
            self.left.pre()

        if self.right is not None:
            self.right.pre()
    def post(self): #Постфиксный подход
        if self.left is not None:
            self.left.post()

        if self.right is not None:
            self.right.post()
        print(self.value)
    def in(self): #Инфиксный подход
        if self.left is not None:
            self.left.in()
        print(self.value)
        if self.right is not None:
            self.right.in
a = Tree(2).left1(7).right1(5) #Создание дерева
b7 = a.left.left1(2).right1(6)
b6 = b7.right.left1(5).right1(11)
b5 = a.right.right1(9)
b9 = b5.right.left1(4)
a.pre()
