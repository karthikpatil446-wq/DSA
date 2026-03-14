price=float(input("enter price of product:"))
discount_percent=int(input("enter discount percentage:"))
discount=(price*discount_percent)/100
final_price=price-discount
print("price of the product:",final_price)

