units=int(input("Enter electricity units consumed: "))
bill=0
if units<=100:
    bill=units*1.5
elif units<=200:
    bill=(100*1.5)+(units-100)*2.5
else:
    bill=(100*1.5)+(100*2.5)+(units-200)*4
print("Total Electricity Bill = ₹", bill)

#Enter electricity units consumed: 50
#Total Electricity Bill = ₹ 75.0