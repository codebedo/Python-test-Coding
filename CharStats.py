class StatsOfChar:
    def character(self, char, puan, unvan):
        self.char = char
        self.puan = puan
        self.unvan = unvan

    def get_unvan(self):

        if self.puan < 3 :
            return f"{self.char}'un {self.puan}'ı bu ve {self.unvan} 'a sahip"
        if self.puan < 5 and  self.puan > 3:
            return f"{self.char}'un {self.puan}'ı bu ve {self.unvan} 'a sahip"

        if self.puan > 4:
            return f"{self.char}'un {self.puan}'ı bu ve {self.unvan} 'a sahip"