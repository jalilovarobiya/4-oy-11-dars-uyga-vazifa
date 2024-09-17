class Telefon:
    def __init__(self, nom, model) -> None:
        self.nomi = nom
        self.modeli = model

    def __str__(self) -> str:
        return f"Nomi: {self.nomi}, modeli: {self.modeli}"
    
class IPhone(Telefon):
    def __init__(self, nom, model, ID) -> None:
        super().__init__(nom, model)
        self.__ID = ID
    
    def id_sini_korish(self) -> str:
        return f"ID: {self.__ID}"
    
    def narx_qoyish(self, yangi_narx) -> str:
        self._narx = yangi_narx

    def narxini_korish(self) -> str:
        return f"Narxi: {self._narx} USD"

class Samsung(Telefon):
    def __init__(self, nom, model, ID) -> None:
        super().__init__(nom, model)
        self.__ID = ID

    def id_sini_korish(self) -> str:
        return f"ID: {self.__ID}"
    
    def narx_qoyish(self, yangi_narx) -> str:
        self._narx = yangi_narx

    def narxini_korish(self) -> str:
        return f"Narxi: {self._narx} USD"

    
telefon1 = IPhone("IPhone", "12Pro max", "AD26505")
telefon2 = Samsung("Sumsung", "Galaxy A03S", "AD57841")
print(telefon1)
print(telefon1.id_sini_korish())
telefon1.narx_qoyish(67800)
print(telefon1.narxini_korish())
print()
print(telefon2)
print(telefon2.id_sini_korish())
telefon2.narx_qoyish(5000)
print(telefon2.narxini_korish())
