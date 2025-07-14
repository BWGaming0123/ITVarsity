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

#Sets
'''
my_set = {1, 2, 3, 4, 5}

print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}
'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set  = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
# Intersection
inter_set = set1.intersection(set2)
print(inter_set)  # Output: {3}

# Difference
diff_set = set1.difference(set2)
print(diff_set)  # Output: {1, 2}