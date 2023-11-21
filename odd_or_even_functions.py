#Exercise 7: Odd_or_even_functions.py

def even_or_odd():
    value = input("What Number? ")
    if int(value) % 2 == 0:
        print(f"{value} is even")
    else:
        print(f"{value} is odd")
even_or_odd()
