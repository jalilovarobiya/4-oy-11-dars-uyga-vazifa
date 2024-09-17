from abc import ABC, abstractmethod

class Telefon(ABC):
    def __init__(self, nom, model) -> None:
        self.nomi = nom 
        self.modeli = model

    @abstractmethod
    def __str__(self) -> str:
        pass

class smartPhone(Telefon):
    def __str__(self) -> str:
        return f"Nomi: {self.nomi}, modeli: {self.modeli}"
    
telefon = smartPhone("iPhone", "13Pro Max")
print(telefon)