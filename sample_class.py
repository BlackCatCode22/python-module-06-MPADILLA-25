# class = cookie cutter
# # object = cookie shape resulted from cookie cutter.

class PartyAnimal:

    def __init__(self):
        self.x = 0

    def party(self):
        self.x = self.x + 1
        print("so far", self.x)

an = PartyAnimal()

# an.party()
# an.party()
# an.party()

print("Type", type(an)) 
print("Dir ", dir(an)) 
print("Type", type(an.x))
print("Type", type(an.party))

# dir(): finds "capabilities" of newly created class.
    # example
x = list()
type(x)
dir(x)
print(dir(x))

# type(): Tells us somethind about a variable.
    # example:
x = list()
type(x)
print(type(x))