# Chapter 7 Exercise 5: Calculator: math-library
import math


def get_numbers():
    while True:
        num = input('Give a number: ')
        try:
            num = int(num)
            return num
        except Exception:
            print('This input is invalid.')


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
    num1 = get_numbers()
    num2 = get_numbers()

    while True:

        print('(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)(7)Change numbers\n(8)Quit\nCurrent numbers:', num1, num2)

        operation = int(input('Please select something (1-6): '))

        if operation in range(1, 7):
            calculate(num1, num2, operation)
        elif operation == 7:
            num1 = get_numbers()
            num2 = get_numbers()
        else:
            print('Thank you!')
            break


if __name__ == '__main__':
    main()
