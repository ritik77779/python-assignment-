# 1. Difference from 17
def diff_17(n):
    if n > 17:
        return 2 * abs(n - 17)
    return abs(n - 17)


# 2. Test range
def test_range(n):
    return (100 <= n <= 1000) or (n == 2000)


# 3. Reverse string
def reverse_string(s):
    return s[::-1]


# 4. Count uppercase & lowercase
def count_case(s):
    result = {"UPPER": 0, "LOWER": 0}
    for char in s:
        if char.isupper():
            result["UPPER"] += 1
        elif char.islower():
            result["LOWER"] += 1
    return result


# 5. Distinct elements in list
def distinct_list(lst):
    return list(set(lst))


# 6. Even numbers from list
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]


# 7. Function inside another function
def robot():
    def move():
        print("Robot is moving...")
    move()


# 8. Function with attributes
def student(name, age, course):
    return f"Name={name}, Age={age}, Course={course}"

student.__defaults__ = ("John", 20, "CS")
print("Function attributes:", student.__code__.co_varnames[:student.__code__.co_argcount])


# 9. Move robot
def move_robot(x, y, direction):
    if direction == "up":
        return (x, y+1)
    elif direction == "down":
        return (x, y-1)
    elif direction == "left":
        return (x-1, y)
    elif direction == "right":
        return (x+1, y)
    else:
        return (x, y)


# 10. Classify temperature
def classify_temperature(temp):
    if temp < 15:
        return "Cold"
    elif 15 <= temp <= 30:
        return "Moderate"
    else:
        return "Hot"


# 11. Goal reached?
def is_goal_reached(path):
    x, y = 0, 0
    for move in path:
        if move == "up": y += 1
        elif move == "down": y -= 1
        elif move == "left": x -= 1
        elif move == "right": x += 1
    return (x, y) == (2, 0)


# 12. Student class with attributes
class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.student_name}, Class: {self.student_class}")


# 13. Student instances
student1 = Student(101, "Alice", "CS")
student2 = Student(102, "Bob", "Math")
student1.display()
student2.display()


# 14. Circle class
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# 15. Class with get_String & print_String
class StringClass:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input("Enter a string: ")

    def print_String(self):
        print(self.s.upper())


# 16. Robot class
class Robot:
    def __init__(self, name, task, battery_level=100):
        self.name = name
        self.task = task
        self.battery_level = battery_level

    def perform_task(self):
        if self.battery_level >= 10:
            print(f"{self.name} is performing task: {self.task}")
            self.battery_level -= 10
        else:
            print(f"{self.name} has low battery! Please recharge.")

    def recharge(self):
        self.battery_level = 100
        print(f"{self.name} is fully recharged!")

    def status(self):
        print(f"Name: {self.name}, Task: {self.task}, Battery: {self.battery_level}%")
