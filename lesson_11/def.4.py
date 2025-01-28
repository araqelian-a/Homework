#Write a python function, which add a new value
#with given key in dict.
def add_value(key,value,dict):
    dict[key] = value
    return(dict)
print(add_value("armen",2005,{"arto":2005,"karen":2004}))