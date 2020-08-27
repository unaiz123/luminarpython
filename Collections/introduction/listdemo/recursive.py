pattern="ABABC"
dict={}

for char in pattern:
    print(char)
    if(char not in dict):
        dict[char]=1
    else:
        print("first rec",char)
        break
