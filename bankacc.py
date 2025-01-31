
class bankacc:
    def __init__(self,acc_holder,acc_no,int_bal=0):
        self.bal = int_bal
        self.acc_holder = acc_holder
        self.acc_no = acc_no

    def withdraw(self,amount):
        if amount > 0:
            if amount < self.bal:
                self.bal -=amount
                print(f"withdraw amount is : {amount}the balance amount is:{self.bal}")
            else:
                print("insufficent balance")

    def deposit(self,amount):
                  if amount > 0:
                      self.bal  += amount
                      print(f"the deposited amount is :{amount} total balance is {self.bal}")
                  else:
                      print("the amount not deposit")

    def check_bal(self):
        print(f"your balance amount : {self.bal}")

def main():
    account = bankacc("sai","07",1000)
    print("account detial")
    account.check_bal()
    print("withdraw the amount")
    account.withdraw(500)
    print("deposit the amount")
    account.deposit(1000)
    # print("the amount of withdraw:"+str(account.withdraw(500))
    # print("the amount of deposit : "+ str(account.deposit(200))
    # print("view the balance amount :"+ str(account.check_bal())

main()

