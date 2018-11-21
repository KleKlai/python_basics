def boolLess(a,b):
	if a < b:
		print(True)
	else:
		print(False)

def boolGreater(a,b):
	if a > b:
		print(True)
	else:
		print(False)

def boolInt(num):
	if str(type(num)) == "<class 'int'>":
		print("Int: "+str(True))

	else:
		print("Int: "+str(False))

def boolFloat(num):
	if str(type(num)) == "<class 'float'>":
		print("Float: "+str(True))
	else:
		print("Float: "+str(False)) 

def boolStr(string):
	if str(type(string)) == "<class 'str'>":
		print("Str: "+str(True))
	else:
		print("Str: "+str(False)) 

def boolIntList(list):
	result = True
	for x in list:
		if str(x) != "<class 'int'>":
			result = False
			break
	print("List Pure Float: "+str(result))

def boolFloatList(list):
	result = True
	for x in list:
		if str(x) != "<class 'float'>":
			result = False
			break
	print("List Pure Float: "+str(result))

def boolStrList(list):
	result = True
	for x in list:
		if str(x) != "<class 'str'>":
			result = False
			break
	print("List Pure Float: "+str(result))

boolLess(2,4)
boolGreater(2,4)
boolInt(45)
boolFloat(3.5)
boolStr("Hi")
boolIntList(list((1,2.3,2)))
boolFloatList(list((1.2,5,4.5,45)))
boolStrList(list(("Hello", 0,"Hi")))

print(str(type(True)))
