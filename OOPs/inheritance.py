# MULTILEVEL
class parent:
    def m1(self):
        print("Parent")

class Child(parent):
    def m2(self):
        print("child")

class SubChild(Child):
    def m3(self):
        print("subchild")

ch=parent()
ch.m1()

c=Child()
c.m1()
c.m2()


su=SubChild()
su.m1()
su.m2()
su.m3()
