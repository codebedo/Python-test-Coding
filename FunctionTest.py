class character:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def say_hi(self):
        print(f"Hello , ı am {self.name} and {self.age} years old")




k1 = character("Bedo", 24)
k1.say_hi()


k2 = character("honey", 24)
k2.say_hi()