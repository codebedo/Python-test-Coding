class volume:
    def __init__(self, app, user, uvolume):
        self.app = app
        self.user = user
        self.uvolume = uvolume


    def volume_cont(self):
        print(f"hello {self.user} Please which one  {self.app}'tu you change the volume")
        
        try:
            print("Please enter the volume")
            target_volume = int(input("Please enter a number"))
        except ValueError:
            print("Please enter a number")
        current_volume = self.uvolume
        if current_volume > target_volume:
            while current_volume > target_volume:
                current_volume -= 1
                print(current_volume)

        elif current_volume < target_volume:
            while current_volume < target_volume:
                current_volume += 1
                print(current_volume)

        else:
            print(f" Volume is already at desired {self.uvolume} level.")



k1 = volume("insta", "bedo", 30)
k1.volume_cont()