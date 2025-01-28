#Given a real number, round it to the nearest whole.
tiv = float(input("tur "))
h = tiv - int(tiv)
if h >= 0.5:
    print(int(tiv) + 1)
else:
    print(int(tiv))
