import re
pateern="[^a-zA-Z1-9]"
matcher=re.finditer(pateern,"ab^^a123*(&baggga789$$00baba!@babakja")
count=0
for match in matcher:
    print(match.start())
    print(match.group())

    count+=1
print("Count :",count)