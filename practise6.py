# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# num4 = int(input("Enter number 4: "))

# if(num1>num4):
#     f1 = num1
# else:
#     f1 = num4

# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3

# if(f1>f2):
#     print(str(f1), "is greatest")
# else:
#     print(str(f2), "is greatest")

# sub1 = int(input("Enter marks of sub1\n"))
# sub2 = int(input("Enter marks of sub2\n"))
# sub3 = int(input("Enter marks of sub3\n"))

# if(sub1<33 or sub2<33 or sub3<33):
#     print("Fail because marks is less than 33")
# elif((sub1+sub2+sub3)/3<40):
#     print("Fail because percentage is less than 40%")
# else:
#     print("Congratulations! You passed the test")



# text = input("Enter the text\n")

# if("make money" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("subscribe now" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This text is spam")
# else:
#     print("This text is not a spam")


# text = input("Enter the text\n")
# if(len(text)>10):
#     print("Given text has more characters than 10")
# else:
#     print("Characters are not more than 10")

# names = ["harry", "shubham", "rohan", "aditi", "shipra"]
# name = input("Enter the name to check\n")

# if(name in names):
#     print("Your name is present in the list")
# else:
#     print("Your name i snot present in the list")


marks = int(input("Enter your marks\n"))

if(marks>=90):
    grade = "EX"
elif(marks>=80):
    grade = "A"
elif(marks>=70):
    grade = "B"
elif(marks>=60):
    grade = "C"
elif(marks>=50):
    grade = "D"
else:
    grade = "F"

print("Your grade is", grade)
