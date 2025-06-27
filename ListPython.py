class ListEx:
    def __init__(self, name: str, roll: int):
        self.name = name
        self.roll = roll



a = [ListEx(name, roll) for name, roll in [('Akash', 2), ('Deependra', 40), ('Reaper', 44), ('Veer', 67)]]


for obj in a:
    print(obj.name, obj.roll, sep=' ')







