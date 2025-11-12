#tuple
my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))
print("Original Tuple : ", my_tuple)

print("Accessing elements:")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

print("Slicing Tuple : ", my_tuple[1:4])
print("Length of Tuple : ", len(my_tuple))

print("Converting Tuple to List")
my_list = list(my_tuple)
print("List : ", my_list)

print("Appending 6 to List")
my_list.append(6)# example
my_list = [1, 2, 3, 4, 5]
print(type(my_list))
print("Original List : ", my_list)
print("Accessing elements:")
print("First element:", my_list[0])
print("Last element:", my_list[-1]) 
print("Slicing List : ", my_list[1:4])
print("Length of List : ", len(my_list))    
print("Appending 6 to List")
my_list.append(6)
print("Updated List : ", my_list)   
print("Removing 2 from List")
my_list.remove(2)
print("Final List : ", my_list)
print("Reversed List : ", my_list[::-1])
print("Updated List : ", my_list)

print("Removing 2 from List")
my_list.remove(2)
print("Final List : ", my_list)

print("Reversed List : ", my_list[::-1])