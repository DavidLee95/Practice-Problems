import numpy

def digit_check():

    while True:
        try:
            number = int(input("Please write the decimal place you want up until 10: "))
        except ValueError:
            print("Please answer with numbers only")
        else:
            if number < 10:
                break
            else:
                print("Please only write numbers up to 10")
    
    value = round(numpy.pi, number)
    print(value)

if __name__ == '__main__':
    digit_check()