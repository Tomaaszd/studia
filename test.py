class Charakter:
    def __init__(self, hp, name, type, position):
        self.hp = hp
        self.name = name
        self.type = type
        self.position = position

    def move(self, dx, dy):
        x, y = self.position
        self.position = (x + dx, y + dy)

    def interakcja(self):
        print(f"{self.name} ({self.type}) wchodzi w interakcję.")

    def show_character(self):
        print(f"Imię: {self.name}")
        print(f"Typ: {self.type}")
        print(f"HP: {self.hp}")
        print(f"Pozycja: {self.position}")
