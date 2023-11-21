def display_num(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    quotient = num1 / num2
    product = num1 * num2

    print("The sum of", num1 ,"and" ,num2, "is equal to", sum)
    print("The difference of", num1, "and", num2, "is equal to", difference)
    print("The quotient of", num1, "and", num2, "is equal to", quotient)
    print("The product of", num1, "and", num2, "is equal to", product)

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
display_num(num1, num2)
