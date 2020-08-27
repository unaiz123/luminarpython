sub={"maths":10,"english":1,"arabic":25,"dsp":9,"microwave":12}
print(sub)
# marks=dict.fromkeys(sub,0)
# print(marks)
for item in sub.items():
    print(item)
print("Finals...................")
print(list(sorted(sub.items())))
print("Max : ",max(sub.values()))

