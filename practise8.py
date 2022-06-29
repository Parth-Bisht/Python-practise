# def maximum(num1, num2, num3):
#     if(num1>num3):
#         if(num1>num2):
#             return num1
#         else:
#             return num2
#     else:
#         if(num3>num2):
#             return num3
#         else:
#             return num2

# m = maximum(14,12,3)
# print(m)

# def farh(cel):
#     return (cel* (9/5)) + 32

# c = 0
# f = farh(c)
# print("Fahrenheit Temperature is " + str(f) + " F") 

# def sum_recursive(n):
#     if(n==0 or n==1):
#         return 1
#     return n + sum_recursive(n-1)

# s = sum_recursive(10)
# print(s)

# n = 6
# for i in range(n):
#     print("*" * (n-i))


def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Hello my darling      "   
n = remove_and_split(this, "my")
print(n)