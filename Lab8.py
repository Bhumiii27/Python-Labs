import math

# 1. Convert degrees to radians
degree = 180
radian = math.radians(degree)
print("1) Degree to Radian:")
print(f"{degree} degrees = {radian} radians")
print()

# 2. Calculate y = 6x^2 + 4sin(x)
x = math.pi / 2   # you can change x here
y = 6 * (x ** 2) + 4 * math.sin(x)
print("2) Formula y = 6x^2 + 4sin(x):")
print(f"For x = {x}, y = {y}")
print()

# 3. f(x), f'(x), f''(x)
def evaluate_functions(x):
    f = math.cos(2 * x)
    f1 = -2 * math.sin(2 * x)
    f2 = -4 * math.cos(2 * x)
    return f, f1, f2

x_val = math.pi
f, f1, f2 = evaluate_functions(x_val)
print("3) Function evaluations at x = π:")
print(f"f(x)   = {f}")
print(f"f'(x)  = {f1}")
print(f"f''(x) = {f2}")
