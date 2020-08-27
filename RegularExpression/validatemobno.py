from re import *

# rule='[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
rule='\d{10}'
mobno=input("enter mob no : ")
matcher=fullmatch(rule,mobno)

if matcher !=None :
    print("Valid  "+mobno)
else:
    print("Invalid  "+mobno)