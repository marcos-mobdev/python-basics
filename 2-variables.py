#Basics
name = "Marcos"
age = 22
height = 1.73
isMale = True
hobbies = ["yoga", "paiting", "games"]

#Useful
jobInfo = {"position" : "Senior Analyst", "wage" : 1200}
friends = ("John", "Katerine", "Bruce")
favoriteFruits = {"Pear", "Watermelon", "Grape"}
myBirthdaysUntilNow = range(age)
partner = None

#Casual
vowels = frozenset({"a", "e", "i", "o", "u"})
complexVariable = 1j+3
bytesVariable = b"Hello"
byteArrayVariable = bytearray(5)
memoryViewVariable = memoryview(bytes(5))

#Prints
print(name,type(name))
print(age,type(age))
print(height,type(height))
print(isMale,type(isMale))
print(hobbies,type(hobbies))

print(jobInfo,type(jobInfo))
print(friends,type(friends))
print(favoriteFruits,type(favoriteFruits))
print(myBirthdaysUntilNow,type(myBirthdaysUntilNow))
print(partner,type(partner))

print(vowels,type(vowels))
print(complexVariable,type(complexVariable))
print(bytesVariable,type(bytesVariable))
print(byteArrayVariable,type(byteArrayVariable))
print(memoryViewVariable,type(memoryViewVariable))

#Parsing

myString = str(1234567890)
myInt = int(20.0)
myFloat = float(20)
myComplex = complex(1)
myList = list(("pencil", "eraser", "book"))
myTuple = tuple(("pencil", "eraser", "book"))
myDict = dict(name="John", age=33)
mySet = set(("pencil", "eraser", "book"))
myBool = bool(4)
myBytes = bytes(5)
myByteArray = bytearray(5)
myMemoryView = memoryview(bytes(5))