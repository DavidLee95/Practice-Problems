dict_org = {1:'Celsius', 2:'USD', 3:'KG', 4: 'KM'}
dict_fin = {1:'Fahrenheit', 2:'MXN', 3:'LBS', 4: 'MILES'}

def convert():
    original_val = org_value()
    final_val = fin_value()
    
    while True:
        try:
            value = int(input('Write the value to be converted'))
        except ValueError:
            print('Only numbers are accepted!')
        else:
            break

    if original_val == final_val == 1:
        value_two = (value*9/5)+32
        print(f'{value} degrees in {dict_org[original_val]} is {value_two} degrees in {dict_fin[final_val]}')
    
    elif original_val == final_val == 2:
        value_two = value*20.39
        print(f'{value} {dict_org[original_val]} is {value_two} {dict_fin[final_val]}')
    
    elif original_val == final_val == 3:
        value_two = value*2.20
        print(f'{value} {dict_org[original_val]} is {value_two} {dict_fin[final_val]}')
    
    elif original_val == final_val == 4:
        value_two = value*0.62
        print(f'{value} {dict_org[original_val]} is {value_two} {dict_fin[final_val]}')
    
    else:
        print(f'{dict_org[original_val]} and {dict_fin[final_val]} are not compatible!')

def org_value():    
    while True: 
        try:
            original_value = int(userinput('In which unit is the original value? Choose the number\n1. CELSIUS\n2. USD\n3. KG\n4. KM\n'))
        except ValueError:
            print('Only numbers are accepted!')
        else:
            if 0< original_value <= 4:
                return(original_value)
                break
            else:
                print('Please select a valid option!')

def fin_value():  
    while True:
        try:  
            final_value = int(userinput('In which unit is the final value? Choose the number\n1. FAHRENHEIT\n2. MXN\n3. LBS\n4. MILES\n'))
        except ValueError:
            print('Only numbers are accepted')
        else:
            if 0 < final_value <= 4:
                return(final_value)
                break
            else:
                print('Please select a valid option!')

def userinput(text):
    answer = input(text).upper()
    return(answer)


if __name__ == '__main__':
    convert()