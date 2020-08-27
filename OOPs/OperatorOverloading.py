class Book:
    def __init__(self,pages):
        self.pages=pages

    def __str__(self):
        return str(self.pages)

    def __add__(self, other):
        return Book(self.pages+other.pages)

    def __sub__(self, other):
        return (self.pages-other.pages)
obj=Book(100)
obj2=Book(200)
ob3=Book(50)
print(obj+obj2)
print(obj2-obj)
print(obj+obj2+ob3)
print(obj+obj2-ob3)