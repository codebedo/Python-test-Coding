# creating string(immutable

s = "Merhaba"
print("Original string: ", s)


# characters indeks acces
print("second character:", s[1]) # 'e'


# string birleştire (new string creating)
s2 = s + "Woeld"
print("combined strings", s2)

# strings length

print("Length:", len(s2))

# Characters singled returned
chars = list(s2)

print("Cahracter list:", chars)

# each one characters printing( array mind set)
print("Eah one characters:")
for c in chars:
    print(c, end=" ")
# string immutable example

s2[0] = "m" # this gone taking issue because strings are not changed
