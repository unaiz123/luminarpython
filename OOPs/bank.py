
import datetime

class Person():
    def setValue(self,name,bank):
        self.name=name
        self.bank=bank
    def Print(self):
        print("A",self.name)
        print("b",self.bank)

class bank(Person):
    def __init__(self,acno,bal):
        self.acno=acno
        # self.name=name
        self.bal=bal
        # self.bankname=bankname
    def Deposite(self,deposit):
        self.deposie=deposit
        self.bal=deposit+self.bal
        print("Current Deposited amonut : ",self.deposie)
        print("Rupees ",self.deposie,"is credited to your Account on ",datetime.date.today())
        print("Total Balance : ",self.bal)

    def Withdraw(self,withdraw):
        self.withdraw=withdraw
        self.withdraw=self.bal-withdraw
        print("Current Withdrawal Amount : ",withdraw)
        if(withdraw>self.bal):
            print("Insufficient Balance,Please Check your Balance")

        else:
            print("Rupees ",withdraw,"is Debited from your Account on ",datetime.date.today())
            self.bal=self.bal-withdraw
            print("Total Balance : ",self.bal)

    def BalanceAmount(self):
        print("Acount Balance Details")
        print("Balance Amount : ",self.bal)

    def PrintDetails(self):
        print("A/C No: ",self.acno)
        print("Name : ",self.name)
        print("Bank : ",self.bank)


obj=bank(12,0)
obj.Deposite(int(input("enter deposit amount : ")))
obj.Withdraw(int(input("enter withdrawal amount : ")))
obj.setValue("Unaiz","Federal")
obj.Print()
obj.PrintDetails()
obj.BalanceAmount()
