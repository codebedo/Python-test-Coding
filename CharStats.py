class StatsOfChar:
    def __init__(self, char, puan):
        self.char = char
        self.puan = puan


    def get_unvan(self):

        if self.puan < 3:
            return "Acemi"
        elif 3 <= self.puan <5:
            return "Usta"

        else:
            return "Efsane"

    def bilgi_göster(self):
        unvan = self.get_unvan()
        print(f"{self.char}'un puanı: {self.puan} ve unvanı: {unvan}")


k2 = StatsOfChar("Bedo", 2)
k2.bilgi_göster()