# num = int(input("Enter the number\n"))
# for i in range(1, 11):
#     print(str(num) + "X" + str(i) + "=" + str(num*i))
#     print(f"{num}X{i}={num*i}")


# li = ["Harry", "Sohan", "Sachin", "Rahul"]

# for item in li:
#     if item.startswith("S"):
#         print("Hello! " + item)

# num = int(input("Enter the number: "))
# prime = True
# for i in range(2, num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime:
#     print("This number is prime")
# else:
#     print("This number is not prime")

# num = int(input("Enter the number: "))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial * i
# print(f"The factorial of {num} is {factorial}")



# for i in range(20):
#     print("*" * (i+1))

n =5
for i in range(5):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
