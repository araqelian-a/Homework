# Create a Python class representing a car with methods for accelerating and braking.
class Car:
    def __init__(self, model, speed=0):
        self.model = model
        self.speed = speed
    def accelear_speed(self,speed):
        self.speed += speed
    def braking(self,brake_speed):
        self.speed -= brake_speed
    def get_speed(self):
        return self.speed
car_1 = Car("Mercedes", 10)
car_1.accelear_speed(50)
print(car_1.get_speed())
car_1.braking(20)
print(car_1.get_speed())
