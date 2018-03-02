def Fibonacci(num):
    

    if num == 0:
        return 0
    elif num <= 2:
        return 1
    else:
        x = 1
        y = 1
        for i in range(2, num):
           temp = y
           y += x
           x = temp
        return y
    

number = int(input("Enter a number: "))
print(Fibonacci(number))
