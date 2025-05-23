"""  
Solution1 (with pre-defined variables):
1. Create two variables, num1 and num2, and assign them the values 12 and 6 respectively.
2. Create a variable sum and assign it the sum of num1 and num2.
3. Print the result using the format method to display the message: "The sum of {num1} and {num2} is {sum}".
"""
num1 = 12
num2 = 6
sum = num1 + num2
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))
# The sum of 12 and 6 is 18


"""
Solution2 (with user input):
1. Prompt the user to enter two numbers using the input function and assign them to num1 and num2.
2. Convert the input values to integers.
3. Create a variable sum and assign it the sum of num1 and num2.
4. Print the result using the format method to display the message: "The sum of {num1} and {num2} is {sum}".
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum of {0} and {1} is {2}".format(num1, num2, sum))
# The sum of 12 and 6 is 18