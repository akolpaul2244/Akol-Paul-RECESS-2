#for loop

favorite_colors = []

number_of_colors = int(input("How may colors are your favorite \n"))

for i in range(number_of_colors):
    color = input(f"Enter favorite color #{i + 1}: ")
    favorite_colors.append(color)

# Print the list of favorite colors
print("Your favorite colors are:", favorite_colors)



#while loop
# Initialize an empty list to store the reversed colors
reversed_colors = []

# Initialize the index for the while loop
index = len(favorite_colors) - 1

# Use a while loop to create the reversed list
while index >= 0:
    reversed_colors.append(favorite_colors[index])
    index -= 1

# Print the original and reversed list of favorite colors
print("Your favorite colors in reverse order are:", reversed_colors)