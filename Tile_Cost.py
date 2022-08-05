def tile_price():
    while True:
        try:
            width = int(input("Please write the width of the area: "))
        except ValueError:
            print('Please only write numbers!')
        else:
            break

    while True:
        try:
            height = int(input("Please write the height of the area: "))
        except ValueError:
            print('Please only write numbers!')
        else:
            break

    while True:
        try:
            price = int(input("Please write the price of the tile per square meter in USD: "))
        except ValueError:
            print('Please only write numbers!')
        else:
            break
    
    total_area = width*height
    total_cost = total_area*price
    print(f'The total area is: {total_area}')
    print(f'The total cost is: {total_cost} USD')

if __name__ == '__main__':
    tile_price()
