#Write a python program which concat 2 dicts
def connect_dict(dict1, dict2):
    for k, v in dict1.items():
        dict2[k] = v

    return dict2

print(connect_dict({"a": 200, "b": 400}, {"c": 100, "d": 8}))


