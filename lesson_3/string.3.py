#Write a Python program to remove the n-th index character from a nonempty string
x="Hayastan"
n=3
x=x[0:n]+x[n+1:]
print(x)