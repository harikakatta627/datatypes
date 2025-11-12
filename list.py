# example
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