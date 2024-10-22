# version1

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# gcd = 0

# minimum = min(num1, num2)

# for i in range(1, minimum + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i

# print(f"the GCD of {num1} and {num2} is {gcd}")

########################

# version2

# def gcd(a, b):
#     return a if b == 0 else gcd(b, a % b)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}.")