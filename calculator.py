# Class som skapar datatypen miniräknkare
# Sends in user input and tests for

class Kaffekopp:
    def __init__(self, Name):
        self.name = Name
        self.position = (0,0,0)
        self.mängdKaffeI = 0
    
    def PrintKopp(self):
        print("Name: " + self.name)
        print("position: " + str(self.position) )
        print("MängdKaffe: " + str(self.mängdKaffeI))
        


kopp1 = Kaffekopp("köpp1")

kopp1.position = (5, 1, 0)
kopp1.mängdKaffeI = 10

kopp2 = Kaffekopp("köpp2")
kopp2.position = (5, 1, 0)
kopp2.mängdKaffeI = 10



kopp1.PrintKopp()
kopp2.PrintKopp()