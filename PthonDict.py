import pandas as pd


"""thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020

}

for j in thisdict:
    for i in thisdict:
        print(i, j)
# type show for type of dictinory
print(type(thisdict))
"""

# the dict() constructor to make a dicitonary


thisdict = dict(name = "Bedo", age="23", Title="Developer")
df = pd.DataFrame(thisdict.items(), columns=["key", "Value"])

print(df.to_string(index=False))
