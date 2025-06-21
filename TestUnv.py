class char:
    def __init__(self, char, puan):
        self.char = char
        self.puan = puan


    def get_unvan(self):

        if 1 < self.puan :
            return "Acemi"
        elif 3 < self.puan < 5:
            return  "Usta"
        else:
            return "Efsane"

    def bilgi_göster(self):
        unvan = self.get_unvan()
        print(f"{self.char}'ın {self.puan} puanı ile {self.get_unvan()} ünvanina hak verildi")




b1 = char("Bedo" , 2)

b1.bilgi_göster()