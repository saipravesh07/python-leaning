class vehicle:
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model
    def move(self):
        print("move")
class car(vehicle):
    pass

class boat(vehicle):
    def move(self):
        print("sail")
class plane(vehicle):
    def move(self):
        print("fly")
mycar = car("ford","2022")
myboat = boat("bmw","2020")
myplane = plane("mnm","2000")
for x in (mycar,myboat,myplane):
    print(x.brand)
    print(x.model)
    x.move()