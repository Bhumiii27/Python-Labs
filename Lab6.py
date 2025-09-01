# a. 
print("a) Odd numbers between 1 to 100:")
i = 1
while i <= 100:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
print("\n")

# b. 
print("b) Sum of natural numbers from 1 to n")
n = int(input("Enter n: "))
total = 0
for i in range(1, n+1):
    total += i
print("Sum =", total, "\n")

# c. 
print("c) Count number of digits in a number")
def count_digits(num):
    return len(str(num))

num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num), "\n")

# d. 
print("d) First and Last digits of a number")
num = int(input("Enter a number: "))
num_str = str(num)
print("First digit:", num_str[0])
print("Last digit:", num_str[-1], "\n")

# e. 
print("e) Swap first and last digits of a number")
num = int(input("Enter a number: "))
num_str = str(num)
if len(num_str) == 1:
    swapped = num_str
else:
    swapped = num_str[-1] + num_str[1:-1] + num_str[0]
print("Number after swapping:", swapped, "\n")

# f. 
print("f) Product of digits of a number")
num = int(input("Enter a number: "))
product = 1
for digit in str(num):
    product *= int(digit)
print("Product of digits:", product, "\n")

# g. 
print("g) Reverse of a number")
num = int(input("Enter a number: "))
reverse = str(num)[::-1]
print("Reverse:", reverse)
