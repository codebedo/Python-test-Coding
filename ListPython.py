class ListEx:
    def __init__(self, name: str, roll: int):
        self.name = name
        self.roll = roll


a = []
#a = [ListEx(name, roll) for name, roll in [('Akash', 2), ('Deependra', 40), ('Reaper', 44), ('Veer', 67)]]
# Map example ,
#a = list(map(lambda x: ListEx(x[0], x[1]), [('Akash', 2), ('Deependra', 40), ('Reaper', 44), ('Veer', 67)]))
# Using Extend()  method efficently adds multiple objects to a lis in a single step.
#its more effcient than appending each object indiviually, as it avoids overhead of resizing the list multiple times
a.extend([ListEx('Akash', 2), ListEx('Deependra', 2), ListEx('Reaper', 44), ListEx('Veer', 67)])

for obj in a:
    print(obj.name, obj.roll, sep=' ')







