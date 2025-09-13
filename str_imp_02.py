# creating strings

s = "hello"
print("origin", s)


# printing each one char

for i, c in enumerate(s):
    print(f"chars {i}. ", c)

# new string creating (immutable example)

s2 = s + " World"

print("New String: ", s2)

# length and index checked
print("Length:", len(s2))
print("Third char", s2[2])