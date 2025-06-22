class StatsOfChar:
    USTA_MIN = 3
    USTA_MAX = 4
    EFSANE_MIN = 5

    def __init__(self, char: str, puan: int)-> None:
        self.char = char
        self.puan = puan


    def get_unvan(self) -> str:

        if self.puan < self.USTA_MIN:
            return "Acemi"
        elif self.USTA_MIN <= self.USTA_MAX <5:
            return "Usta"

        else:
            return "Efsane"

    def bilgi_göster(self)-> None:
        print(str(self))

    def __str__(self)->str:
        return f"{self.char}' un puanı: {self.puan} ve unvanı: {self.get_unvan()}"
    


k2 = StatsOfChar("Bedo", 2)
k2.bilgi_göster()