quantity = int(input("How much you want to buy: "))
pricePerUnit= 100
if quantity >1000:
    print("your total cost is",(quantity*pricePerUnit)*10/100-quantity)
else:
    print("your total cost is",quantity*pricePerUnit)