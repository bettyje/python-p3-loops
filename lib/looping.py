#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")
# happy_new_year()


def square_integers(int_list):
    return [i ** 2 for i in int_list]
print(square_integers([1, 2, 3, 4, 5])) 


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Calling the function
fizzbuzz()

    