"""the_world_is_flat = True

if the_world_is_flat:
    print("Be carefull the world is flat\n")



i = 5

def f(arg=i):
    print(arg)
i = 6
f()"""


def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))