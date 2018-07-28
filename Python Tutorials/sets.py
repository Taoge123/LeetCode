Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun","Mon"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}

for d in Days:
    print(d)


Days.add("Sunjnkn")
print(Days)

tony = set([1,2,])
rika = set([12,3,123,2,2,4,234,2,34324])

print(tony | rika)
print(tony & rika)
