strs = ["sunflower", "sunny", "sun"]


prefix = strs[0]

for word in strs[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
        if prefix == "":
            break

print(prefix)


