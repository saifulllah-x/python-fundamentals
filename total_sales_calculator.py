# Total Sales Calculator
# Takes a product name, quantity sold and price per unit,
# then prints the total sales amount.

print('Total Sales Calculator')
product = input("Product Name: ")
quantity = int(input("Enter quantity sold: "))
price_per_unit = float(input("Enter price per unit: "))

total_sales = quantity * price_per_unit

print("Product:", product)
print("Total Sales Amount =", total_sales)
