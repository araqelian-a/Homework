# Write a function that validates a URL string. Handle the ValueError by raising a custom
# exception if the URL format is invalid.
from urllib.parse import urlparse
def url_stugum(string):
    string = urlparse(string)
    if string.scheme and string.netloc:
        print("it is URL")
    else:
        raise ValueError("this is not URL")
url_stugum("https://api.example.com/v1/products/12345")
