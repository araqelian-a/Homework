# Write a simple login system where the user enters a username and password. Handle
# the KeyError by raising a custom exception if the username is not found in the users
# database(dictionary).
baza_dict = {"Ashot": 1234, "Arsen": 14}
def login_eror(name,password):
    if name not in baza_dict:
        raise Exception(f"{name}-anunov user chka")
    if baza_dict[name] == password:
        print("bari galust")
    else:
        print("sxal parol")
try:
    login = "Ashot"
    password = 1234
    login_eror(login, password)
except:
    print("chka tenc user")

