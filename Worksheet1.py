# 1. Print string in specific format
print("""Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are""")

# 2. Accept user's first and last name and print in reverse order
first = input("Enter your first name: ")
last = input("Enter your last name: ")
print(last + " " + first)

# 3. Area of circle based on radius
import math
r = float(input("Enter radius of circle: "))
print("Area of circle =", math.pi * r * r)

# 4. Display first and last colors from list
color_list = ["Red", "Green", "White", "Black"]
print("First color:", color_list[0])
print("Last color:", color_list[-1])

# 5. Compute n+nn+nnn
n = int(input("Enter a number: "))
result = n + int(str(n)*2) + int(str(n)*3)
print("Result:", result)

# 6. Generate list and tuple from comma-separated numbers
values = input("Enter comma-separated numbers: ")
lst = values.split(",")
tpl = tuple(lst)
print("List:", lst)
print("Tuple:", tpl)

# 7. Convert Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)

# 8. Swap two numbers (with increment in one variable)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping: a =", a, "b =", b)
a, b = b, a + 1   # increment added to swapped 'a'
print("After swapping: a =", a, "b =", b)

# 9. Check odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 10. Check leap year
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 11. Euclidean distance between two coordinates
import math
x1, y1 = map(float, input("Enter first coordinate (x1 y1): ").split())
x2, y2 = map(float, input("Enter second coordinate (x2 y2): ").split())
dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean Distance =", dist)

# 12. Check if 3 angles form a triangle
a1 = int(input("Enter first angle: "))
a2 = int(input("Enter second angle: "))
a3 = int(input("Enter third angle: "))
if a1 + a2 + a3 == 180:
    print("It is a triangle")
else:
    print("Not a triangle")

# 13. Compound interest
p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (years): "))
ci = p * (pow((1 + r / 100), t)) - p
print("Compound Interest =", ci)

# 14. Check prime number
n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# 15. Sum of squares 1² + 2² + ... + N²
N = int(input("Enter a number: "))
total = sum(i**2 for i in range(1, N+1))
print("Sum of squares =", total)
