# Dictionary
# A dictionary is a collection of key-value pairs where each key is unique and maps to a specific value. Dictionaries are commonly used in programming to store and retrieve data efficiently based on keys.
# Example 

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(type(my_dict))
print("Original Dictionary : ", my_dict)

print("Accessing elements:")
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

print("Length of Dictionary : ", len(my_dict))
print("Adding a new key-value pair (country: USA)")
my_dict["country"] = "USA"
print("Updated Dictionary : ", my_dict)

print("Removing the key 'age' from Dictionary")
del my_dict["age"]
print("Final Dictionary : ", my_dict)

print("Keys in Dictionary : ", list(my_dict.keys()))

print("Values in Dictionary : ", list(my_dict.values()))

print("Items in Dictionary : ", list(my_dict.items()))

print("Clearing the Dictionary")
my_dict.clear()
print("Cleared Dictionary : ", my_dict)
