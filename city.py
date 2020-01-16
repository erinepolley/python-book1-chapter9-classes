class City:
    def __init__(self, name, mayor, year):
        self.name = name
        self.mayor = mayor
        self.year = year
        self.buildings = []
    def add_building(self,building):
        self.buildings.append(building)
