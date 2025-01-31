# dep = ("cse","ece","eee","bba")
# it = iter(dep)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
#
#


class num1:
    def __iter__(self):
        self.a =1
        return self

    def __next__(self):
        if self.a<=20:
         x= self.a
         self.a+=1
         return x
mynum1 = num1()
myiter = iter(mynum1)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


