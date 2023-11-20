#EXERCISE 3 Odd or Even
#Create a python program that determines if the number is Odd or even based on the user input

value = input("What Number? ")
if int(value) % 2 == 0:
    print(f"{value} is even")
else:
    print(f"{value} is odd")
