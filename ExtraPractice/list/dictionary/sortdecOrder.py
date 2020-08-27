# sub={"maths":10,"english":1,"arabic":25,"dsp":9,"microwave":12}
#
# print(sorted(sub))
# print(sorted(sub, reverse=True))

#sorting highest mark.............

student={
    ('alis',50,18),('anu',75,12),('arun',75,20),("jimmy",90,20),('john',45,12)
}

# def sorter(item):
#     error=100-item[1]
#     age=item[2]
#     return (error,age)
#
# sorted_ist=sorted(student,key=sorter)
# print(sorted_ist)

sorted_list=sorted(student,key=lambda i:(100-i[1],i[2]))
print(sorted_list)