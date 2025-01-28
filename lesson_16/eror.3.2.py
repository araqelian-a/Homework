# Write a function that validates a URL string. Handle the ValueError by raising a custom
# exception if the URL format is invalid.
def url_stugum(string):
     if not string.startswith("http" or "https"):
         raise ValueError("it is not URL")
     if " " in string:
         raise ValueError("it is not URL")
     string = string.split(".")
     if len(string[-1]) == 0:
         raise ValueError("it is not URL")
     print("This is URL")
url_stugum("https://api.example.com")


