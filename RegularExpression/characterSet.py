from re import *

#pattern='[^0-9A-Za-z]'
#pattern='[a-z]
#pattern='[A-Z]
pattern='[\d]'
matcher=finditer(pattern,"AAVVVBabdsdkaAABBG54LK8@$^&()&^%909400499-20-2--2FFJJdlkkaabckkcccliw")
for match in matcher:
    print(match.start())
    print(match.group())