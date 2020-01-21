class Person(object):
    species = "Homo Sapien"
    def __init__(self, name, email='no email', phone='no phone'):
        self.name = name 
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0 
        self.person_greeted = []

    def __str__(self):
        return f"Person: {self.name} {self.email} {self.phone}"

    def greet(self, other_person): # other_person must be a class instance with name attribute
        print(f"Hello {other_person.name}, I am {self.name}.")
        self.greeting_count += 1
        if other_person not in self.person_greeted:
            self.person_greeted.append(other_person)

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    def add_friend(self, person):
        self.friends.append(person)

    def num_freinds(self):
        print(len(self.friends))

    def num_unique_people_greeted(self):
        print(len(self.person_greeted))
        

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
# dee_ann = Person('Dee Ann', 'dee-ann@gmail.com', '555-555-5550')
dee_ann = Person('Dee Ann')

sonny.greet(jordan)
sonny.num_unique_people_greeted()
sonny.greet(jordan)
sonny.num_unique_people_greeted()
sonny.greet(dee_ann)
sonny.num_unique_people_greeted()



class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.year, self.make, self.model)

leaf = Vehicle('Nissan', 'Leaf', 2015)
# leaf.print_info()
