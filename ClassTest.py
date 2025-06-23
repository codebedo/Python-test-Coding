class Title:
    def __init__(self, name:str , age : int) ->None:
        self.name = name
        self.age = age



    def take_info(self)->None:
        User_name = self.name
        User_age = self.age

        User_name = input(print("Please enter the user name"))
        User_age = int(input("Please enter the user age"))
    def show_info(self)->None:

        print(f"{self.take_info()} , {self.age}")







k1 = Title(None, None)
k1.show_info()