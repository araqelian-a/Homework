# Write a function that checks if a given string is a valid email address.
def valid_email(email):
    if "@" not in email:
        raise ValueError("this is not email address")
    if " " in email:
        raise ValueError("this is not email address")
    part = email.split("@")
    for i in part:
        if i == "":
            raise ValueError("this is not email address")
    part_2 = email.split(".")
    last_part = part_2[-1]
    if not last_part.isalpha():
        raise ValueError("this is not email address")
email = "asdsadsad@mail.ru"
valid_email(email)
