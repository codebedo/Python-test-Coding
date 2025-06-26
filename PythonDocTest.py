"""the_world_is_flat = True

if the_world_is_flat:
    print("Be carefull the world is flat\n")



i = 5

def f(arg=i):
    print(arg)
i = 6
f()"""
"""

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))"""


def f_none(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f_none(5))
print(f_none(7))
print(f_none(8))