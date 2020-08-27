employee={
    "eid":1002,
    "ename":"person",
    "desig":"tester",
    "salary":15000,

}

print(employee["ename"])
print("company" in employee)
employee["company"]="luminar"
employee["salary"]+=5000
for key in employee:
    print(key,":",employee[key])
print(employee)
