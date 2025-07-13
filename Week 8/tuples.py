my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)  # Output: 1
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3
print(my_tuple[-1])  # Output: 5

# Tuples are immutable, so we cannot change their values

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6) 

conc_tuple = tuple1 + tuple2 # Concatenation
rep_tuple = tuple1 * 3  # Repetition
print(conc_tuple)  # Output: (1, 2, 3, 4, 5, 6)
print(rep_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)