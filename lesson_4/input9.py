#You are given four real numbers - the coordinates of two points on a
#plane. The first two numbers are the x and y coordinates of the first point,
#and the last two numbers are the x and y coordinates of the second point.
#Output the length of the line segment bounded by the two points.
import math
x = int(input("tur arajini cordinaty "))
y = int(input("tur arajini 2rd cordinaty "))
x1 = int(input("tur erkrordi cordinaty "))
y2 = int(input("tur erkrordi 2rd cordinaty "))
heravorutyun = (((x1 - x) ** 2+(y2 - y) ** 2))**0.5
print(heravorutyun)