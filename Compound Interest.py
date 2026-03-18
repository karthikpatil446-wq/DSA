p=float(input("enter principal amount:"))
t=float(input("enter time (in months):"))
r=float(input("enter rate of intrest (%):"))
t=t/12
si=(p*t*r)/100
amount=p*(1+r/100)**t
ci=amount-p
print("total  amount=",amount)
print("Compound Interest:",ci)
print("simple intrest:",si)