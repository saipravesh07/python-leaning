class school:
    def __init__(self,name,id,marks):
        self.name = name
        self.id = id
        self.marks = marks

    def studentdetails(self):
        print(self.name+ str( self.id)+ str( self.marks))

class student(school):
    pass
stud = student("john",77,99)
stud.studentdetails()