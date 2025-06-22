class volume:
    def __init__(self, app, user, uvolume):
        self.app = app
        self.user = user
        self.uvolume = uvolume


    def volume_cont(self):
        print(f"hello {self.user} Please which one  {self.app}'tu you change the volume")
        print("Please enter the volume")
        volume = int(input())
        if self.uvolume > volume:
            while volume <= self.uvolume:
                volume -= 1
                print(volume)
                if volume == self.uvolume:
                    break
        else:
            while volume >= self.uvolume:
                volume += 1
                print(volume)
                if volume == self.uvolume:
                    break



k1 = volume("insta", "bedo", 20)
k1.volume_cont()