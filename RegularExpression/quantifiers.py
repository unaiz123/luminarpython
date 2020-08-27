from re import *
#pattern='[\D]'
#pattern='a+'
#pattern="a*"
#pattern="a?"
#pattern="a{2}"
pattern="a{1,4}"
matcher=finditer(pattern,"aklJJHSaaNSNIUDaamhlaaakllkglflaaa679240j5allaokllj5laaalla5#$^**^%jhhh$%^")
for match in matcher:
    print(match.start())
    print(match.group())