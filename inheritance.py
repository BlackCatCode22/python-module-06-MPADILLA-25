# Inheritance - Creating a new class by reusing an existing class and its capabilities.
    # Adding own bit to inherited class makes new class. 

# stores in another form to be reused. Class can be written once but reused many times. 

# New class - Child
# Old class - Parent

class PartyAnimal :

    def __init__(self, nam) :
        self.x = 0
        self.name = nam
        print(self.name, "constructed")

    def party(self) :
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal) : # This class will inherit everything from PA.

    def __init__(self, nam) :
        super().__init__(nam)
        self.points = 0

    def touchdown(self) :
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()