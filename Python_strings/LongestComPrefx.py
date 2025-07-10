"""strs = ["sunflower", "sunny", "sun"]


prefix = strs[0]

for word in strs[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
        if prefix == "":
            break

print(prefix)
"""

strc = ["apple", "apricot", "apcenter", "approach"]


prefex = strc[0]

for word in strc[1:]:
    while not word.startswith(prefex):
        prefex = prefex[:-1]
        if prefex == "":
            break

print(prefex)