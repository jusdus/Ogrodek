from abc import abstractmethod, ABC

class Uprawa(ABC):
    def __init__(self, nazwa):
        self.ogrod = None  # przy sadzeniu zostanie ustawiony przez ogrod
        self.nazwa = nazwa
        self.waga = 1
        self.wilgotnosc = 10
        self.wiek = 0
        self.polozenie = 0

    def rosnij(self, dni):
        # możemu tutaj zmienić wiek uprawy, bo to niezależy od jej rodzaju
        pass

    @abstractmethod
    def podlej(self, litry):
        if self.wilgotnosc < 100:
            self.waga += 5
            self.wilgotnosc += litry
        else:
            return False

    def opis(self):
        # można stworzyć opis z tego co już mamy
        pass

    @abstractmethod
    def obszar(self):
        #rectangle
        pass

    @abstractmethod
    def narysuj(self, skala, poziom_ziemi):
        #pyglet
        pass


