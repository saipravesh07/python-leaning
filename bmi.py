def bmi_cal():
    weight = int(input("enter the weight:"))
    hight = float(input("enter the hight:"))
    bmi = (weight / hight ** 2)
    print("your bmi is "+str(bmi))
bmi_cal()
