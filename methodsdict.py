myDict = {
    "fast" : "In a quick manner",
    "parth" : "A Coder",
    "marks" : [1,22,55],
    "anotherDict" : {'parth' : 'player'},
    1:2
}

print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(myDict)
updateDict = {
    "ganel" :"friend",
    "hero" : "heroism",
    "zero" : "even number"
}
myDict.update(updateDict)
print(myDict)
# print(myDict.get("parth2")) #prints none
# print(myDict["parth2"]) #throws error because not available