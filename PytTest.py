class Test:

    def __init__(self, work: str , id: int):

        self.work = work
        self.id = id


    def show_inf(self):
        print(f"{self.work}, {self.id} we have now this")





k1 = Test("Testing" , 1)

k1.show_inf()