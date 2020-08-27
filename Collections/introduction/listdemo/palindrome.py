num=input("enter input : ")

if((num[0])==(num[-1])):
    if((num[1])==num[-2]):
        print("ITS PALINDROME")
    else:
        print("ITS NOT PALINDROME ")
else:
    print("ITS NOT PALINDROME")