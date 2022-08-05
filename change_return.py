def change_cal():
    change_coins = []

    while True:
        try:
            cost = float(input("What is the total cost in USD?"))
        except ValueError:
            print('Only numbers are accepted')
        else:
            break
    
    while True:
        try:
            amount = float(input("How much will you pay in USD?"))
        except ValueError:
            print('Only numbers are accepted!')
        else:
            if amount >= cost:
                break
            else:
                print('The amount to be paid has to be greater than the cost!')

    change = amount - cost
    print(change)
    change_2 = change - int(change)

    while change_2 >= .25:
        change_coins.append('quarter')
        change_2 -= .25
    
    while .25 > change_2 >= .10:
        change_coins.append('dime')
        change_2 -= .10
    
    while .10 > change_2 >= .05:
        change_coins.append('nickel')
        change_2 -= .05
    
    while .05 > change_2 > 0:
        change_coins.append('penny')
        change_2 -= .01

    quarters = change_coins.count('quarter')
    dimes = change_coins.count('dime')
    nickels = change_coins.count('nickel')
    pennies = change_coins.count('penny')
    print(f'The coins that will be given are the following:\nQuarters: {quarters}\nDimes: {dimes}\nNickels: {nickels}\nPennies: {pennies}')

if __name__ == '__main__':
    change_cal()
