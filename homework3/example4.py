num = int(input("Enter a number: "))
sum_of_powers = 0

num_digits = len(str(num)) 

for digit in str(num):
    sum_of_powers += int(digit) ** num_digits

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
