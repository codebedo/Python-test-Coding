class Test:
    def __init__(self, target: int, start: int)->None:
        self.target = target
        self.start = start



    def for_loop(self):
        starting = self.start
        Target = self.target

        for starting in range(Target):
            print(self.start + 1)








k1 = Test(10, 2)

k1.for_loop()