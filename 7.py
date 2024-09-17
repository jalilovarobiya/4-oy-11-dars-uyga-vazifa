class Telefon:
    def __init__(self, brend, model):
        self.brend = brend
        self.model = model
        
    def kiritish(self):
        self.brend = input("Telefon brendni kiriting: ")
        self.model = int(input("Telefon modelini kiriting: "))
      
    def chiqarish(self):
        print(f"Telefon brend: {self.brend}")
        print(f"modeli: {self.model}")
       
Telefon1 = Telefon("iPhone", "XV ProMax")
Telefon2 = Telefon("Samsung", "Galaxy A03S")

Telefon1.chiqarish()
Telefon2.chiqarish()