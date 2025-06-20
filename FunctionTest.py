class character:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


    def say_hi(self):
        print(f"Hello , ı am {self.name} and {self.age} years old")


    def talk_back(self):
        print(f"Hey  {self.name} whatsupp?")

    def convert_secont(self):
        print("How is the job")

    def say_som(self):
        print(f"{self.job} something is fun")



k1 = character("Bedo", 24, "developer")
k1.say_hi()
k1.talk_back()
k1.convert_secont()
k1.say_som()


