# Given two dictionaries, merge them into a new dictionary, excluding any keys
# that start with an underscore.
dict1 = {"h": 4, "_e": 1, "y": 6}
dict2 = {'d': 4, '_i': 5, 'f': 6}
merge_dict = {k: v for d in (dict1, dict2) for k, v in d.items() if not k.startswith("_")}
print(merge_dict)
