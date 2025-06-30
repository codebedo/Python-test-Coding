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



thisdict = dict( name = "CodeBedo" , age="23", Title = "Developer")
df = pd.DataFrame(thisdict.items(), columns=["key", "Value"])

print(df.to_string(index=False))



thisdict01 = dict(job = "Developing", id = "2", Title ="Workiingface")
df01 = pd.DataFrame(thisdict01.items(), columns=["key", "Value"])

print(df01.to_string(index=True))

attributes = 'A,B,C'
def get_Example():
    for value in all_example:
        yield  dict(zip(attributes, value.strip().replace("",'').split(',')))


print(lst)

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


li = [("Fruits", "Apple"), ("Fruits", "Banana"), ("Vegetables", "Carrot")]
d = {}

for k, item in li:
    d.setdefault(k, []).append(item)

print(d)

li = [("Fruits", "Apple"), ("Fruits", "Banana"), ("Vegetables", "Carrot")]




"""

# Roll Back dictionary

d1 ={'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {}

for key, value in d1.items():
    d2[value] = key

print(d1)

print(d2)


d3 = {'one': 1, 'two':2, 'three': 3}
d4 = {}

for key, value in d3.items():
    d4[value] = key
    print(d4)


print(d3)
print(d4)



d5 = {'one': 1, 'two':2, 'three': 3}
d6 = {}

for key , value in d5.items():
    d6[value] = key
    print(d6)

print(d5)
print(d6)