from re import *

rule='\w*[@]gmail[.]com'

email=input("Enter Email ID  for Validation : ")
matcher=fullmatch(rule,email)

if matcher !=None:
    print("Valid Email id : "+email )
else:
    print("Invalid Email id : "+email)