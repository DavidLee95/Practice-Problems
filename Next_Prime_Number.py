def prime_num():
    number = 1
    prime_list = []

    while True:
        try:
            user = int(input('How many prime numbers do you want to find: '))
        except ValueError:
            print('Please only write whole numbers')
        else:
            break

    while len(prime_list) < user:
        prime = 0
        for n in range(1,number+1):
            if number%n == 0:
                prime += 1
        if prime == 2:
            prime_list.append(number)
        number += 1
    print(prime_list)

if __name__ == '__main__':
    prime_num()
    

