def total_mark():
    total_mark = sub1 + sub2 + sub3 + sub4 + sub5
    print(total_mark)
    percenage = int(total_mark * 100 / 500)
    print(percenage)
    grade(percenage)
def grade(percenage):
    if percenage > 90:
        print("the grade is A")
    elif percenage > 80:
        print("the grade is B")
    elif percenage >70:
        print("the grade is C ")
    elif percenage >60:
        print("the grade is D")
    elif percenage < 50:
        print("fail")
std_id = int(input("enter the student id"))
std_name = input("enter student name")
sub1 = int(input("enter the maths marks"))
sub2 = int(input("enter the english marks"))
sub3 = int(input("enter the tamil marks"))
sub4 = int(input("enter the hindi marks"))
sub5 = int(input("enter the sst marks"))
total_mark()
