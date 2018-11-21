def stringUpper(string):
	string = str(string).upper()
	print(string)

def stringLower(string):
	string = str(string).lower()
	print(string)

def stringLength(string):
	print(len(string))

def stringConcat(string1,string2):
	print(str(string1)+", "+str(string2))

def stringIntStr(num):
	num = str(num)
	print(num, end=" --> ")
	print(str(type(num)))

def stringFloatStr(num):
	num = str(num)
	print(num, end=" --> ")
	print(str(type(num)))

def stringProfanity(string,filters):
	if filters in string:
		string = string.replace(filters, "****")
		print(string)

def stringDisplay(string):
	print(str(string))

def stringTypeInt(int):
	print(str(type(int)))

def stringTypeFloat(float):
	print(str(type(float)))

def stringTypeStr(string):
	print(str(type(string)))

def stringTypeBool(bool):
	print(str(type(bool)))

def stringTypeList(list):
	print(str(type(list)))

def stringList(string):
	print(list((string[slice(0,len(string))])))

def stringTuple(string):
	print(tuple((string[slice(0,len(string))])))

def stringSet(string):
	print(set((string[slice(0,len(string))])))

def stringListString(list):
	for x in list:
		print(x,end="")
	print()

def stringTupleString(tuple):
	for x in tuple:
		print(x,end=" ")
	print()

def stringLoop(string):
	for x in string:
		print(x,end=" ")
	print()

def stringRemove(string,remove):
	if remove in string:
		string = string.replace(remove, "")
		print(string)

def stringUpdate(string,update,replace):
	if update in string:
		string = string.replace(update, replace)
		print(string)



stringUpper("Hello")
stringLower("HELLO")
stringLength("Hello")
stringConcat("Hello","World")
stringIntStr(int(456))
stringFloatStr(float(4.5))
stringProfanity(str("I wanna fuck"),str("fuck"))
stringRemove("I wanna fuck",str("fuck"))
stringUpdate("I wanna fuck",str("fuck"),str("hug"))
stringDisplay("Hello")
stringTypeInt(3)
stringTypeFloat(4.5)
stringTypeBool(True)
stringTypeList(list((1,2,3)))
stringList("Hello")
stringTuple("Hello")
stringSet("Hello")
stringListString(list(("H","E","L","L","O")))
stringTupleString(tuple(("W","O","R","L","D")))
stringLoop("Hello")



