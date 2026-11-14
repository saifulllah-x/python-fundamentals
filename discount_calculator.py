# Discount Price Calculator
# Takes an item name, its original price and a discount percentage,
# then prints the final price after the discount.

print('Discount Price Calculator')
item = input("Enter Item Name: ")
price = float(input("Original Price: "))
discount = float(input("Discount Percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Final Price of", item, "=", final_price)
