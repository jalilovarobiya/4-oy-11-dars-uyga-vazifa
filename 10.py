class Telefon:
    def __init__(self, ID, narx, tezkor_xotira_hajm) -> None:
        self.__id = ID
        self._narxi = narx
        self.tezkor_xotira_hajmi = tezkor_xotira_hajm

    def __str__(self) -> str:
        return f"ID: {self.__id}, narxi: {self._narxi}, tezkor xotira hajmi: {self.tezkor_xotira_hajmi} GB"
    
telefon = Telefon("AD26505", 20000, 8)
print(telefon)