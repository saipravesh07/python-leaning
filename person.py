class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def get_name(self):
        return self.name
class employee:
    def __init__(self,job):
         self.job = job
    def get_job(self):
        return self.job

class manger(person,employee):
    def __init__(self,name,job):
