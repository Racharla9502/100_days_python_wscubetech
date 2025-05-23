#Solution1 - (using exponention)

num = 64
num1= int(input("Enter a number: "))

sr = num**(1/2)
print("The square root of", num, "is", sr)


#Solution2 - (using math module)
import math
num2= int(input("Enter a number: "))
sr1 = math.sqrt(num2)
print("The square root of", num2, "is", sr1)