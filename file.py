# f = open('sample.txt','r')
f = open('sample.txt') #by default the mode is r
# data = f.read()
#data = f.readline() #read one line
data = f.read(5) #read first five characters
# print(data)
f.close()

f = open('another.txt', 'a')
f.write(" I am appending")
f.close()


with open('another.txt', 'w') as f:
    a = f.write("me")
print(a)
with open('another.txt', 'r') as f:
    a = f.read("me")
print(a)