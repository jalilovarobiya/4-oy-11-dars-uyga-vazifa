class Telefon:
    def __init__(self, nomi, modeli) -> None:
        self.nom = nomi
        self.model = modeli

    def chiqarish(self):
        return f"Telefon: {self.nom}, model: {self.model}"

class IPhone(Telefon):
    def __init__(self, nomi, modeli) -> None:
        super().__init__(nomi, modeli) 

class Samsung(Telefon):
    def __init__(self, nomi, modeli) -> None:
        super().__init__(nomi, modeli)

telefon = Samsung("iPhone", "X")
print(telefon.chiqarish())