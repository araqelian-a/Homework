#Create a string made of the first, middle and last character of given string with odd number of
#symbols
x="Armenia"
h=len(x)/2
x=x[0]+x[int(h)] +x[-1]
print (x)