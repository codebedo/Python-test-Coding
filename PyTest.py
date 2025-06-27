class Test:
    def __init__(self, name: str, title: str, id: int):
        self.name = name
        self.title = title
        self.id = id
        self.character = []

    def add_character(self):
        self.character.append(f"{self.name} , {self.title} ,{self.id}")

    def show_all(self):
        characters = self.character

        for i in range(characters):
            print(i)


k1 = Test("bedo", "programmer", 1)



k1.show_all()
