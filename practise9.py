# f = open('poem.txt')
# t = f.read()
# if 'twinkle' in t:
#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")
# f.close()

# def game():
#     return 110

# score = game()
# with open("highscore.txt") as f:
#     highscore = f.read()
# if highscore=="":
#     with open("highscore.txt", "w") as f:
#         f.write(str(score))
# elif int(highscore)<score  :
#     with open("highscore.txt", "w") as f:
#         f.write(str(score))


# for i in range (2,21):
#     with open(f"Tables/Multiplication_table_of_{i}.txt", 'w') as f:
#         for j in range(1, 11):
#             f.write(f"{i}X{j}={i*j}\n")
#             break


# with open('sample.txt') as f:
#     content = f.read()

# content = content.replace("donkey", "$$#@#$")
# with open ('sample.txt', 'w') as f:
#      f.write(content)

words = ["mote", "saale", "kaddu"]

with open('sample.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#^$#^$%")
    with open('sample.txt', 'w') as f:
        f.write(content)
