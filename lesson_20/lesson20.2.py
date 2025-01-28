# Create a Python class representing a basic calculator with methods for addition,
# subtraction, multiplication, and division.
class Calculator:
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return self.num + other.num
    def __sub__(self, other):
        return self.num - other.num
    def __mul__(self, other):
        return self.num * other.num
    def __truediv__(self, other):
        return self.num / other.num
obj_1 = Calculator(5)
obj_2 = Calculator(8)
print(obj_1 / obj_2)
print(obj_1 * obj_2)
print(obj_1 + obj_2)
print(obj_1 - obj_2)