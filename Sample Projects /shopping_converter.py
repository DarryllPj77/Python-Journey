#Simple Shopping Calculator with Currency Converter
item = str(input("What item would you like to buy?: "))
price = float(input("What is the price?: "))
quantity = int(input("How many would you like to buy?: "))
total = price * quantity
print(f"The item you buy is {item} ")
print(f"The price of the {item} is ${price} ")
print(f"I would like to buy {quantity} {item} ")
print(f"The total price for {quantity} {item} is: ${round(total,2)}!") #use round for 2 decimal places
#currency converter
dollar = total * 1
peso = total * 56

print(f"The price in $Dollars is: ${dollar}")
print(f"The price in ₱Peso is:  ₱{peso}")
