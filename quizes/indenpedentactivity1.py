# 1. Create a simple list variable that contains 5 list items.

favorite_colors = ['blue', 'green', 'red', 'yellow', 'purple']

# 2. Find and print the specific item in each list based on their index in the list

# find and print index 3
print(zoo_animals[3])

# find and print index 1
print(sports_on_tv[1])

# find and print index 0
print(random_numbers[0])

# 3. Create a program that will only print out the odd numbers in this list.

# HINT- part of solving this is that you will need to use the range() function.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in number_list:
    if num % 2 != 0:
        print(num)

# 4. Fix the shopping cart function.

# HINT - for this function you will need to use the append() function.

new_item = input("Enter the item you want to add to the shopping cart: ")
shopping_cart.append(new_item)
print("Updated Shopping Cart:", shopping_cart)
Note: In the fourth prompt, the code uses the input() function to get user input for a new item to be added to the shopping cart. This assumes that the code is being run interactively, allowing the user to input data during execution. If you are running the script without user interaction, you may want to modify this part accordingly.






Regenerate
