class Vehicle:
    def __init__(self, name, kind, color, value):
        self.name = name
        self.color = color
        self.kind = kind
        self.value = value
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
   
car1 = Vehicle("Nick", "cadillac", "white", 50000.00)
car2 = Vehicle("Jump", "van", "blue", 10000.00)

print(car1.description())
print(car2.description())
