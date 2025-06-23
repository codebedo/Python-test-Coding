import json


class Character:
    def __init__(self, name:str, score: int)->None:
        self.name = name
        self.score = score

    @property
    def title(self)->str:
        if self.score <3 :
            return "Acemi"
        if 3 <= self.score < 5:
            return "Usta"
        else:
            return "Efsane"

    def show_info(self)->None:
        print(f"{self.name}'s Score = {self.score}, Titles = {self.title}")



class CharacterManager:
    def __init__(self)->None:
        self.characters = []

    def add_character(self, name:str, score: int)->None:
        self.characters.append(Character(name,score))

    def show_all(self)->None:
        for char in self.characters:
            char.show_info()




def get_character_input(manager: CharacterManager):
    while True:
        name = input("Please enter character Nae (fot the exit 'q':")
        if name.lower() == 'q':
            break
        try:
            score = int(input(f"{name} : please enter the score (0-10) : "))
            manager.add_character(name, score)
        except ValueError:
                print("You entered wrong number, Please enter the number.")


def save_to_file(manager: CharacterManager, filename: str):
    data = [{"name": c.name, "scıre": c.score} for c in manager.characters]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_from_file(manager: CharacterManager, filename:str):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            for entry in data:
                manager.add_character(entry["name"], entry["score"])
    except FileNotFoundError:
        print("File not found, Creating new lists")



if __name__ == "__main__":
    manager = CharacterManager()
    load_from_file(manager, "Character2.json")
    get_character_input(manager)
    manager.show_all()
    save_to_file(manager, "Character2.json")