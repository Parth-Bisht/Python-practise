n = 6
product = 1
for i in range(n):
    product = product*(i+1)
print(product)

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product*(i+1)
    return(product)

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(5)
print(f)

def factorial(n):
    product = 1
    for i in range(n):
        product = product*(i+1)
    return(product)

def maximum(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num2
    else:
        if(num3>num2):
            return num3
        else:
            return num2