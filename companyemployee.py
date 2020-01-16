from companies import Company
from employees import Employee

erin = Employee("Erin Polley", "software developer", "April 27, 2020")
corri = Employee("Corri Golden", "front end engineer", "June 3, 2020")
chase = Employee("Chase Fite", "software engineer", "April 12, 2020")
matt = Employee("Matthew Blagg", "software developer", "May 7, 2020")
guy = Employee("Guy Cherkesky", "company mogul", "March 23, 2020")

eventbrite = Company("EventBrite", "Cummins Station", "Tech")
asurion = Company("Asurion", "Downtown", "Insurance")

asurion.add_people([chase, guy])
eventbrite.add_people([erin, matt, corri])

def print_stuff(business):
    print(f'{business.name} is in the {business.type} industry and has the following employees:') 
    for employee in business.employees:
        print(f'*{employee.name}')

print_stuff(asurion)
print_stuff(eventbrite)
