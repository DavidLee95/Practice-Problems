def card_check():
    number = card_number()
    print(f'The credit card number is: {str(number)[0:4]}-{str(number)[4:8]}-{str(number)[8:12]}-{str(number)[12:16]}' )
    converted_value = check_sum(number)
    first_sum = compare_value(converted_value)
    second_sum = first_sum + int(str(number)[15])
    if second_sum%10 == 0:
        print('The card is valid')
    else:
        print('The card is invalid')

def card_number():
    while True:
        try:
            number = int(input('Enter the 16 digits of your credit card:\n'))
        except ValueError:
            print('Only numbers are accepted')
        else:
            if len(str(number)) == 16:
                break
            elif len(str(number)) > 16:
                print('You have entered more than 16 digits')
            else:
                print('You have entered less than 16 digits')
    return(number)
    
def check_sum(number):
    number_str = str(number)
    new_str = ''
    for i in range(0,len(number_str)-1):
        if i%2 == 0:
            new_str += str(int(number_str[i])*2)
        else:
            new_str += number_str[i]

    return(new_str)

def compare_value(converted_value):
    sum = 0
    for i in converted_value:
        sum += int(i)
    return(sum)

if __name__ == '__main__':
    card_check()