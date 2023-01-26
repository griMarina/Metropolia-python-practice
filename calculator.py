# Chapter 7 Exercise 5: Calculator: math-library
import math


def calculate(num1, num2, operation):
    if operation == 1:
        res = num1 + num2
    elif operation == 2:
        res = num1 - num2
    elif operation == 3:
        res = num1 * num2
    elif operation == 4:
        res = num1 / num2
    elif operation == 5:
        res = math.sin(num1/num2)
    else:
        res = math.cos(num1/num2)
    print('The result is:', res)


def main():
    print('Calculator')

    num1 = int(input('Give the first number: '))
    num2 = int(input('Give the second number: '))

    while True:

        print('(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)(7)Change numbers\n(8)Quit\nCurrent numbers:', num1, num2)

        operation = int(input('Please select something (1-6): '))

        if operation in range(1, 7):
            calculate(num1, num2, operation)
        elif operation == 7:
            num1 = int(input('Give the first number: '))
            num2 = int(input('Give the second number: '))
        else:
            print('Thank you!')
            break


if __name__ == '__main__':
    main()
