class Company:
    def __init__(self, name, address, typeof):
        self.name = name
        self.address = address
        self.type = typeof
        self.employees = []
    def add_people(self, employeeList):
            self.employees.extend(employeeList)
            # print(self.employees)

