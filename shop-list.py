# Chapter 10 Exercise 2: Using the list

def askUser():
    operation = input(
        'Would you like to \n(1)Add or\n(2)Remove items or\n(3)Quit?: ')
    return operation


def addItem(shop_list):
    item = input('What will be added?: ')
    shop_list.append(item)


def removeItem(shop_list):
    print(f'There are {len(shop_list)} items in the list.')
    index = int(input('Which item is deleted?: '))
    if index >= len(shop_list):
        print('Incorrect selection.')
    else:
        shop_list.pop(index)


def main():
    shop_list = []
    while True:
        operation = askUser()
        if operation == '1':
            addItem(shop_list)
        elif operation == '2':
            removeItem(shop_list)
        elif operation == '3':
            print('The following items remain in the list:')
            for item in shop_list:
                print(item)
            break
        else:
            print('Incorrect selection.')


if __name__ == '__main__':
    main()
