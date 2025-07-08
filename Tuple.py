# Tuples are hashable"""
"""
coords = set()

#a = [1,2] # [] -> () yaparsan problem çözülür
#b = [2,2]
""""""
a = (1, 2)
b = (2, 2)
coords.add(a)
coords.add(a)
coords.add(a)
coords.add(a)
coords.add(a)
print(coords)
"""""""""

# Memory Sharing

#a= [1,2] # if we changing [] -> () like this they sharing the memorys
#b = [2,2]

a = (1,2)
b = (2,2)

print(id(a)) #id memory pointer
print(id(b))