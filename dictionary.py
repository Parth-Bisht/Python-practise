myDict = {
    "Fast" : "In a quick manner",
    "Parth" : "A Coder",
    "Marks" : [1,22,55],
    "anotherDict" : {'parth' : 'player'}
}

print(type(myDict['Fast']))
print(myDict['Parth'])
myDict['Marks'] = [45,56]
print(type(myDict['Marks']))
print(type(myDict['anotherDict']))