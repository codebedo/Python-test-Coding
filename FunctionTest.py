class character:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def say_hi(self):
        print(f"Hello , ı am {self.name} and {self.age} years old")


    def talk_back(self):
        print(f"Hey  {self.name} whatsupp?")




k1 = character("Bedo", 24)
k1.say_hi()
k1.talk_back()


