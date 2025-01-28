from string import ascii_letters
from string import digits
from string import punctuation
import random
h = "asd"
x = str("".join(random.choices(ascii_letters)))
print(h + x)