from re import *
#pattern='[\D]'
pattern="The rain in india,unexpected rain and wid,rain make somany disorders.rain distrois somany houses"
# matcher=findall("somany",pattern)
matcher=search("\s",pattern)
print(matcher.start())
print(matcher.group())

# matcher=finditer(pattern,"akl JJ HSNSNIUDaam hlgkkglfl6 79240j5ok  j5l5#$^**^%jhhh$%^")
# for match in matcher:
#     print(match.start())
#     print(match.group())