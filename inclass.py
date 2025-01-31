class father():
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def printdetails(self):
        print(self.name,self.address)

class son(father):
    pass
x = son("john","chennai")
x.printdetails()