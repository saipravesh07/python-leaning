number = int(input("Enter a number: "))
def armstrong(number):
    digits = str(number)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    if( sum_of_powers == number):
      print(f"{number} is an Armstrong number.")
    else:
      print(f"{number} is not an Armstrong number.")
armstrong(number)