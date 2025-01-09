"""my_name, my_dep, my_age = "sai" , "ece" , 22
print(my_age)

#global variable and local variable

my_name = "sai"  

def myself():
 my_age = 22
 print(my_age)

myself()

print(my_name) """


def myname():
 global name
 name = "sai"
myname()
print(name)