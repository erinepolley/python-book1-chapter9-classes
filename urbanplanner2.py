from urbanplanner import Building
from city import City

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
        # print(f'{building.address} was purchased by {building.owner} on {building.date_constructed} and has {building.stories} stories.')

construct()

boston = City("Boston", "Sarah Collins", 1689)
for building in buildings:
    boston.add_building(building)
for building in boston.buildings:
    print(f"This building in Boston is owned by {building.owner}, is located at {building.address} and is {building.stories} stories tall")