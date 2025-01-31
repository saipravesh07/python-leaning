class animal:
    def __init__(self,name,):
        self.name = name
    def sound(self):
        print(self.name+" "+"i make this sound")
class dog(animal):
    pass

class cat(animal):
    pass

pets = dog("brk")
ca = cat("miyo")
pets.sound()
ca.sound()