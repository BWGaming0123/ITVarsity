#Advanced concepts - Strings

message = 'Hello World! '

print(message[0])
print(message[1])

print(message[-1])

print(len(message))

print(message.strip()) #Removes whitespace from the beginning and end of the string
print(message.lower()) #Converts the string to lowercase
print(message.split(',')) #Splits the string into a list based on commas

#upper method
print(message.upper()) #Converts the string to uppercase
#replace method
print(message.replace('World', 'Python')) #Replaces 'World' with 'Python'           

num = 3

print(type(num))

num2 = 3.14

print(type(num2))

#varbles

my_variable = 10
total_count = 0
user = 'Jhon'

#Invalid
second_variable = 10
user-name = 20

#Operators

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Modulus (%)
# Exponentiation (**)

x = 10
y = 2

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)

x += 2
x -= 2

str1 = 'Hello'
str2 = 'World'

print(str1 + ' ' + str2)  # Concatenation
print(str1 * 3)  # Repetition

#Control Statements

num = 10

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater than" , num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")

#Loop Control Statements

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break  # Stop the loop for "cherry"
    print(fruit)

for fruit in fruits:
    if fruit == "cherry":
        continue  # Skip the current iteration for "cherry"
    print(fruit)

for fruit in fruits:
    if fruit == "cherry":
        pass  # Do nothing for "cherry"
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 1  # Increment count by 1
    if count == 3:
        break  # Stop the loop when count is 3