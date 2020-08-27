with open("words","r") as f:
    data=f.readlines()
    for i in data:
        word=i.split()
        print(word)