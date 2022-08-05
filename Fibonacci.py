def get_fibonacci():
    a = 0
    b = 1
    
    while True:
        try:
            length = int(input("Determine the length of the sequence up until 20: "))
        except ValueError:
            print("Please write whole numbers")
        else:
            if length > 20:
                print("Choose a number up until 20")
            else:
                break
    
    for n in range(0,length):
        print(a)
        b_0 = b
        b = a + b
        a = b_0

if __name__ == '__main__':
    get_fibonacci()
        
        
