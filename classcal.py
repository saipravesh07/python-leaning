class cal:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        return self.num1 +self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1/self.num2

def main():
  num1 = float(input("enter the number 1"))
  num2 = float(input("enter the number 2"))
  opr = input("choose opr +,-,*,/")
  p1 = cal(num1,num2)
  if opr =="+":
      print(f"Result of :{p1.add()}")
  elif opr == "-":
      print(f"result of :{p1.sub()}")
  elif opr == "*":
      print(f"result of :{p1.mul()}")
  elif opr == "/":
      print(f"result of :{p1.div()}")
  else:
      print("inv")
main()