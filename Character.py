import PythonjsonTest

CharPython = PythonjsonTest.Character
class CharacterManager:
    def __init__(self)->None:
        self.characters = []


    def add_character(self, name: str, score: int)->None:
        self.characters.append(CharPython(name,score))

    def show_all(self) -> None:
        for char in self.characters:
            char.Charpython