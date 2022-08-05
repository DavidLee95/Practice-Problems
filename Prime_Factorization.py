def prime_fac():

    while True:
        try:
            number = int(input("Write the number you want to check: "))
        except ValueError:
            print('Please write numbers only!')
        else:
            break
    
    for n in range (1,number+1):
        prime = 0
        if number%n == 0:
            for n2 in range (1,n+1):
                if n%n2 == 0:
                    prime += 1
            if prime == 2:
                print (n)

if __name__ == '__main__':
    prime_fac()