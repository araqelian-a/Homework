 # Write a function that prompts the user to enter a number and tries to convert it to an
 # integer. Handle the TypeError exception by printing a message indicating that the input
 # is not a valid number. Use a finally block to print "Type conversion process completed."
def input_number():
    try:
        num = float(input("tur tivy="))
        num = int(num)
        print(f"trvacy int = {num}")
    except ValueError:
        print("hnaravor chi int sarqel ")
    finally:
        print("gorcyntacy katarvel e")
input_number()
