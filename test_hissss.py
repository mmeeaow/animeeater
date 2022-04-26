fibo = int(input("Enter final term number of sequence"))

def iterfibo(fibo):
    next_term = 0
    prev_term = 0
    for x in range(0, fibo):  
        if(x == 0):
            next_term = 0
        elif(x == 1):
            prev_term = 1
            next_term = 1
        else:
            temp = next_term
            next_term += prev_term
            prev_term = temp

        print (next_term)

def recurfibo(fibo):
    if fibo in {0, 1}:  # Base case
        return fibo
    return recurfibo(fibo - 1) + recurfibo(fibo - 2)  # Recursive case

for x in range(fibo):
    print(recurfibo(x))


