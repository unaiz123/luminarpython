class Employee:

    def setEmployee(self,eid,ename,desig,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.salary=salary
    def printEmployee(self):
        print(self.eid)
        print(self.ename)
        print(self.desig)
        print(self.salary)

emp=Employee()

emp.setEmployee(1,"unaiz","developrer",25000)
emp.printEmployee()
