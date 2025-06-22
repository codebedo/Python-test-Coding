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


k1 = Character("Bedo", 1)
k1.show_info()