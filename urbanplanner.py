import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = "Erin Polley"
        self.date_constructed = 4
        self.owner = ""
        self.address = address
        self.stories = stories
    def construct(self):
            self.date_constructed = datetime.datetime.now()
    def purchase(self, name):
            self.owner = name

hospital_building = Building("200 Street", 8)
school_building = Building("300 St.", 2)
grocery_building = Building("100 St", 60)
church_building = Building("400 St.", 3)
bar_building = Building("500 St", 89)

buildings = [hospital_building, school_building, grocery_building,
church_building, bar_building] 

def mogul():
    for building in buildings:
        building.purchase("Daisy Gatsby")
        # print(building.owner)

mogul()

def construct():
    for building in buildings:
        building.construct()
        print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories.')

construct()

