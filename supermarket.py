# Chapter 11 Exercise 1: Supermarket

def main():
    prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    total = 0
    print('Supermarket\n===========')

    while True:
        product_num = int(input('Please select product (1-10) 0 to Quit: '))

        if product_num == 0:
            payment = int(input(f'Total: {total}\nPayment: '))
            print('Change:', payment - total)
            break

        product_price = prices[product_num - 1]
        print(f'Product:  {product_num} Price:  {product_price}')
        total += product_price


if __name__ == '__main__':
    main()
