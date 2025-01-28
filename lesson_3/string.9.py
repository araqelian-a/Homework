#Append new string in the middle of a given (even number of characters) string
x="Hayastan"
h=len(x)/2
x=x[0:int(h)]+"new"+x[int(h):]
print (x)
