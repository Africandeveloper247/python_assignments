#This is a python code to calculate discount and price of items

print("Python code to calculate discount price and determine if it is greater than 20 percent")

#create a function
def calculate_discount(price, discount_percent):
    #for discount_percent , we calculate using the formular
    discount= discount_percent/100*price
    new_price = price - discount

    if discount_percent >=20:
        return new_price
    else:
        return price
while True:
    # for prompting users to add price 
    item_price = int(input("Enter your price (N): "))
    price_discount= int(input("Enter your discount(%): "))
    price = item_price
    discount_percent = price_discount
    print(calculate_discount(item_price, price_discount))




