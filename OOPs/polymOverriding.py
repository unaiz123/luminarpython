class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def printVal(self):
        print(self.id)
        print(self.name)
        print(self.sal)

    def __str__(self):
        return self.name


obj1=Employee(101,"UNAIZ",25000)
obj2=Employee(102,"Alsif",25000)
obj3=Employee(103,"Raheem",45000)
obj4=Employee(103,"ssss",5000)
ls=[]

ls.append(obj1)
ls.append(obj2)
ls.append(obj3)
ls.append(obj4)







