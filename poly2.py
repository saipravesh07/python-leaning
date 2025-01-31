class car:
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model
    def move(self):
        print("drive")
class boat:
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model
    def move(self):
        print("sail")
class plane:
    def __init__(self,brand,model):
        self.brand =brand
        self.model =model
    def move(self):
        print("fly")
mycar = car("ford","2022")
myboat = boat("bmw","2020")
myplane = plane("mnm","2000")
for x in (mycar,myboat,myplane):
    x.move()