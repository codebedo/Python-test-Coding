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


"""thisdict = dict(name = "Bedo", age="23", Title="Developer")
df = pd.DataFrame(thisdict.items(), columns=["key", "Value"])

print(df.to_string(index=False))
"""
"""
all_example = ['A,1,1', 'B,2,1', 'C,4,4', 'D,4,5']


lst = [
    {"A":1, "B":2, "C":4, "D":4},
    {"A":1, "B":2, "C":4, "D":5}

]


attributes = 'A,B,C'
def get_Example():
    for value in all_example:
        yield  dict(zip(attributes, value.strip().replace("",'').split(',')))


print(lst)
"""
from collections import  defaultdict
lst01 = {'one', 'two', 'three'}

for i in lst01:
    print(lst01)

d = defaultdict(list)

d[4].append('four')
d[5].append('five')
d[6].append('six')

for j  in d :
    print(d)


