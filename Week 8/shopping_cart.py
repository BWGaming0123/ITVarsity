# Create a shopping cart programme that will continuously ask the user for a food product and its price.
# Have an exit clause if the user wishes to stop adding items.
# At the end, print out the total cost of all items in the cart.

foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy or press q to finish): ")
    if food.lower == 'q':
        break
    else:
        price = float(input(f"Enter price for {food}: R"))
    foods.append(food)
    prices.append(price)


print("------ YOUR CART ------")

for food in foods:
    print(food)
for price in prices:
    total += price

print(f"Your total is: R{total}")