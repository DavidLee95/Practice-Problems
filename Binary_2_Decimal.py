def binary_2_decimal():
    while True:
        try:
            number = int(input("Enter the number you wish to convert: "))
        except:
            print('Only numbers are accepted!')
        else:
            break
    
    number_str = str(number)
    
    while True:
        try:
            option = int(input("Which conversion do you want to do:\n1. Decimal to binary?\n2. Binary to decimal?\n "))
        except:
            print('Only numbers are accepted!')
        else:
            if 0< option < 3:
                break
            else:
                print('Please choose an available option!')
        
    if option == 1:
        def dec_to_bin(n):
            if n > 1:
                dec_to_bin(n // 2)
            print(n % 2, end = '')
        dec_to_bin(number)
                
    
    elif option == 2:
        x = 0
        total_sum = 0
        while x < len(number_str):

            current_number = number_str[-(x+1)]
            value = int(current_number) * (2**x)
            total_sum += value
            x += 1

        print(f'The decimal value is: {total_sum}')


if __name__ == '__main__':
    binary_2_decimal()
            
