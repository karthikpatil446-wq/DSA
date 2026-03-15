value = float(input("Enter real value: "))
percentage= float(input("Enter percentage of depreciation (%): "))

depreciation = value * percentage / 100
final_value = value - depreciation

print("Depreciation Amount =", depreciation)
print("Value after Depreciation =", final_value)
#output
"""Enter real value: 1000
Enter percentage of depreciation (%): 5
Depreciation Amount = 50.0
Value after Depreciation = 950.0"""