# Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3.
lenght_word = {i: len(i) for i in ["barev", "lav", "em", "du", "vonc", "es"] if len(i) > 3}
print(lenght_word)