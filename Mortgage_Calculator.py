def mortgage_calc():

    while True:
        try:
            amount = float(input("Please enter the mortgage amount in USD: "))
        except ValueError:
            print('Only enter numbers')
        else:
            break
    
    while True:
        try:
            years = int(input("Please enter the total years to pay the mortgage: "))
        except ValueError:
            print('Only enter numbers')
        else:
            break

    while True:
        try:
            interest = float(input("Please enter the monthly interest rate: "))*0.01
        except ValueError:
            print('Only enter numbers')
        else:
            break
    
    while True:
        try:
            payments = int(input("Please select one of the following payments:\n1. Monthly\n2. Weekly\n3. Daily\n"))
        except ValueError:
            print('Only enter numbers')
        else:
            if 0 < payments < 4:
                break
            else:
                print('Only select valid options!')
                continue
    
    if payments == 1:
        total_amount = (amount*(interest*((1+interest)**(years*12))))/(((1+interest)**(years*12))-1)
        print(f'The monthly payments in {years} years will be {total_amount} USD')
    elif payments == 2:
        total_amount = ((amount*(interest*((1+interest)**(years*12))))/(((1+interest)**(years*12))-1))*12/52
        print(f'The weekly payments in {years} years will be {total_amount} USD')
    else:
        total_amount = ((amount*(interest*((1+interest)**(years*12))))/(((1+interest)**(years*12))-1))*12/365
        print(f'The daily payments in {years} years will be {total_amount} USD')     

if __name__ == '__main__':
    mortgage_calc()



