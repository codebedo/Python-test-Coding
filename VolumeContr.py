class volume:
    def __init__(self, app, user, uvolume):
        self.app = app
        self.user = user
        self.uvolume = uvolume


    def volume_cont(self):
        print(f"hello {self.user} Please which one  {self.app}'tu you change the volume")
        volume = input("Please wich level")
        if self.uvolume > volume:
            while self.uvolume <= self.volume:
                volume -= 1
                print(self.volume)



k1 = volume("insta", "bedo", "20")
k1.volume_cont()