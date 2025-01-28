#Write a Python function that takes two sets as input and returns a new set containing
#elements that are present in either of the input sets, but not in both.
Names = {"Arto", "Armen", "Arsen", "Arto", "Arsen", "Hayk"}
Names2 = {"Armen", "Karen", "Vardan", "Arsen"}
print(Names ^ Names2)