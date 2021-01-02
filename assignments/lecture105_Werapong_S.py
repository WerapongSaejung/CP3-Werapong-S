class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def tureOnAirConditioner(self):
        print("Turn On : Air")

class car(Vehicle):
    color = ""
car1 = car()
car1.tureOnAirConditioner()
car1.color = "red"

class van(Vehicle):
    width = ""
van1 = van()
van1.tureOnAirConditioner()
van1.width = "1.8 M"

class pickUp(Vehicle):
    capWidth = ""
pickUp1 = pickUp()
pickUp1.tureOnAirConditioner()
pickUp1.capWidth = "2.5 M"

class estateCar(Vehicle):
    turbo = ""
estateCar1 = estateCar()
estateCar1.tureOnAirConditioner()
estateCar1.turbo = "2"