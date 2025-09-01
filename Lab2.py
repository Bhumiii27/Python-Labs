print("----- Rectangle -----")
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
print()


print("----- Even or Odd -----")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
print()


print("----- Cube -----")
side = float(input("Enter the side length of the cube: "))
surface_area = 6 * side**2
volume = side**3
print("Surface area of the cube:", surface_area)
print("Volume of the cube:", volume)
print()


print("----- Equation z = (x + y)*(x - y) -----")
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))
z = (x + y) * (x - y)
print("Value of z:", z)
print()


print("----- Equation z = (x + y)^2 - 2xy -----")
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))
z = (x + y)**2 - 2*x*y

print("Value of z:", z)
print("Comment: This equation is equivalent to x^2 + y^2")
print()


print("----- Celsius to Fahrenheit -----")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")
