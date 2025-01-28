#You are given four real numbers- a1, b1, a2, b2 - The endpoints of two
#line segments on a line. Find the length of their intersection. Note that the
#order of the endpoints of a segment is irrelevant, i.e. the segments [1;2]
#and [2;1] are considered the same.
a1 = float(input("a1="))
a2 = float(input("a2="))
b1 = float(input("b1="))
b2 = float(input("b2="))
if a1 > a2:
    max = a1
    min = a2
else:
    min = a1
    max = a2
if b1 > b2:
    max2 = a1
    min2 = b2
else:
    min2 = b1
    max2 = b2
if min < min2:
    hatum_skizb = min2
else:
    hatum_skizb = min
if max < max2:
    hatum_verj = max
else:
    hatum_verj = max2
if hatum_skizb < hatum_verj:
    print(hatum_verj-hatum_skizb)
else:
    print(0)
