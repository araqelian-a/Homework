# Write a function that performs the following tasks:
# Accepts a list and an index as input.
# Attempts to access the element at the given index in the list.
# Handles both IndexError
# Uses a finally block to print "Task completed" regardless of whether an exception
# occurred or not
def acces_element(list, index):
    try:
        element = list[index]
        print(f"{element},{index}")
    except IndexError:
        print("i dont have this index")
    finally:
        print("Task completed")
list = [1, 2, 10, 40 ]
acces_element(list, 50)