#consession stand program

menu = {"pizza":299,
        "popcorn":80,
        "nachos":60,
        "softdrink":90,
        "egg puff":40,
        "samosa":40,
        "ice cream":70,
        "sweet corn":60
}
cart = []
total = 0
print("-----------MENU-------------")
for key,values in menu.items():
    print(f"{key:13}:{values}/-")

print("----------------------------")

while True:
    food = input("Enter the food you need to buy (q to quit): ").lower().strip()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        print(f"Added {food.title()} to cart.") 
    else:
        print("Item not in menu. Try again.")

print("Cart:", [item.title() for item in cart])
for food in cart:
    total += menu.get(food)
print(f"Your total bill is {total}")