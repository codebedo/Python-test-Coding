class Sms:

    def __init__(self, costumer, number):
        self.costumer = costumer
        self.number = number


    def msg_send(self):

        self.sms_sys()
        print(f"Merhabalar {self.costumer} , size kendimizi hatırlatmak isteriz nakliye hizmetine devam etmekteyiz")




    def sms_sys(self):
      self.number = input(print(f"Please enter the {self.costumer}"))
      print(f"{self.number}")





k1 = Sms("Ülkü", 0)
k1.msg_send()




