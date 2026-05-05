def factorial(num):
    cont = 1
    for i in range(1, num+1):
        cont *= i

    print(cont)

factorial(1) # 1
factorial(2) # 2
factorial(3) # 6
factorial(4) # 24