fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Output: apple

fruits[1] = "blueberry"  # Change the second item
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

fruits = ["apple", "banana", "cherry"]

fruits.append("kiwi")
print(fruits)

fruits.insert(1, "orange")  # Insert at index 1
print(fruits)  

fruits.remove("kiwi")
print(fruits)

fruits.sort(reverse=True)
print(fruits)  