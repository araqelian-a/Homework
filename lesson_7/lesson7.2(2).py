#Count all letters, digits, and special symbols from a given string
# 2rd tarberakna nuyn xndri vor if i mej or chtam
words = input("nermuci texty ")
chars = 0
digits = 0
for i in words:
    if ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122:
        chars = chars + 1
    elif ord(i) >= 48 and ord(i) <= 57:
        digits = digits + 1

print(f"chars = {chars}")
print(f"digits = {digits}")
print(f"symbols = {len(words)-digits-chars}")
print(ord("1"))