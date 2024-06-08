#Create a program that will take product name and price from user and will print an invoice with the product name, price and total amount in console.
product_name = input("Enter product name: ") #We will cover input function in the next topic
price = float(input("Enter price: "))
total_amount = price

# Invoice header
print("*" * 30)
print("         INVOICE")
print("*" * 30)

# Product details
print("Product name:", product_name)
print(f"Price: {price:.2f} INR")

# Total amount
print("-" * 30)
print("Total amount:" + str(total_amount))
print("-" * 30)

# Output:
# Enter product name: Laptop
# Enter price: 45000
# ******************************
#          INVOICE
# ******************************
# Product name: Laptop
# Price: 45000.00 INR
# ------------------------------
# Total amount:45000.0


# In this program, we are taking the product name and price from the user using the input function. We are then printing an invoice with the product name, price and total amount in the console. The total amount is calculated based on the price entered by the user. The output is displayed in the console based on the input entered by the user.

# That's all for the first project in Python. In the next file, we will cover the input functions in Python. (inputs.py)