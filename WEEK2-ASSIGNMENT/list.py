# Created an empty list
my_list = []

print(type(my_list))

# Append the list 10, 20, 30, 40

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(f"My appended list:{my_list}")

# Insert the value 15 at the second position in the list.

my_list[1] = 15

print(f"After insering 15:{my_list}")

# Extend my_list with another list: [50, 60, 70].

my_list.extend([50, 60, 70])

print(f"After extending:{my_list} ")

# Remove the last element from my_list.

del my_list[6]

print(f"After removing the last element:{my_list}")

# Sort my_list in ascending order.

my_list.sort()

print(f"My sorted list in ascending order:{my_list}")


# Find and print the index of the value 30 in my_list.

index= my_list.index(30)

print(f"Finding the index of value 30:Its on index {index}")
