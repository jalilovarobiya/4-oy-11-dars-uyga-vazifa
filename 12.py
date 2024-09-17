# Telefon abstract base class da id_sini_korish, narx_qoyish,
# narxini_korish abstract method lar yarating.
from abc import ABC, abstractmethod

class Telefon(ABC):
    def __init__(self, nom, model) -> None:
        self.nomi = nom 
        self.modeli = model
        self._narx = None

    def __str__(self) -> str:
        return f"Nomi: {self.nomi}\nModeli: {self.modeli}"

class smartPhone(Telefon):
    def __init__(self, nom, model, ID) -> None:
        super().__init__(nom, model)
        self.__ID = ID

    def id_sini_korish(self) -> str:
        return f"ID: {self.__ID}"
    
    def narx_qoyish(self, yangi_narx) -> str:
        self._narx = yangi_narx

    def narxini_korish(self) -> str:
        return f"Narxi: {self._narx} USD"
    
telefon = smartPhone("iPhone", "13Pro Max", "AD26505")
print(telefon)
print(telefon.id_sini_korish())
telefon.narx_qoyish(2000)
print(telefon.narxini_korish())