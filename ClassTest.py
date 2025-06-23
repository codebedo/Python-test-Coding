class Title:
    def __init__(self, name:str , age : int) :
        self.name = name
        self.age = age



    def take_info(self):
        User_name = self.name
        User_age = self.age

        User_name = input(print("Please enter the user name"))
        User_age = int(input("Please enter the user age"))

        print(f"{User_name} , {User_age}")







k1 = Title(None,None)
k1.take_info()