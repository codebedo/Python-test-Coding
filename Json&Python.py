import json
class Character:
    def __init__(self, name: str, score: int)->None:
        self.name = name
        self.score = score


    @property
    def title(self)->str:
        if self.score <3:
            return "Acemi"
        if 3 <= self.score < 5:
            return "Usta"
        else:
            return "Efsane"

    def show_info(self) -> None:
        print(f"{self.name}'in Puani = {self.score}, unvanı = {self.title}")

class CharacterManager:
    def __init__(self)->None:
        self.characters = []

    def add_character(self, name: str, score: int) -> None:
        self.characters.append(Character(name,score))

    def show_all(self) -> None:
        for char in self.characters:
            char.show_info()

def get_character_input(manger: CharacterManager):
    while True:
        name = input("Karakter ismi girin (çıkmak için 'q'): ")
        if name.lower() == 'q':
            break
        try:
            score = int(input(f"{name} için puan girin (0-10): "))
            manger.add_character(name, score)
        except ValueError:
                print("Hatalı puan girdiniz. lütfen Sadece sayi girin.")

def save_to_file(manager: CharacterManager, filename: str):
    data = [{"name": c.name, "score": c.score} for c in manager.characters]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_from_file(manager: CharacterManager, filename: str):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            for entry in data:
                manager.add_character(entry["name"], entry["score"])
    except FileNotFoundError:
        print("Dosya bulunamadı. yeni liste oluşturuluyor")



if __name__ == "__main__":
    manager = CharacterManager()
    load_from_file(manager, "Characters.json")
    get_character_input(manager)
    manager.show_all()
    save_to_file(manager, "characters.json")



