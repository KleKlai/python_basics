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

def boolVerify(bool):
	if str(type(bool)) == "<class 'str'>":
		print("Bool: "+str(False))

	elif str(type(bool)) == "<class 'bool'>":
		print("Bool: "+str(True))
	else:
		print("Bool: "+str(False)) 

def boolListVerify(list):
	if str(type(list)) == "<class 'list'>":
		print("List: "+str(True))
	else:
		print("List: "+str(False)) 

def boolSetVerify(set):
	if str(type(set)) == "<class 'set'>":
		print("Set: "+str(True))
	else:
		print("Set: "+str(False)) 

def boolTupleVerify(tuple):
	if str(type(tuple)) == "<class 'tuple'>":
		print("Tuple: "+str(True))
	else:
		print("Tuple: "+str(False)) 


def boolDictionaryVerify(dictionary):
	if str(type(dictionary)) == "<class 'dictionary'>":
		print("Dictionary: "+str(True))
	else:
		print("Dictionary: "+str(False)) 

def boolIntList(list):
	result = True
	for x in list:
		if str(x) != "<class 'int'>":
			result = False
			break
	print("List Pure Int: "+str(result))

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
	print("List Pure Str: "+str(result))

def boolOdd(num):
	if num % 2 != 0:
		print("Odd:"+str(True))
	else:
		print("Odd:"+str(False))

def boolEven(num):
	if num % 2 == 0:
		print("Even"+str(True))
	else:
		print("Even"+str(False))

def boolRightTriangle(opposite,adjacent,hypotenuse):
	hypotenuse = hypotenuse **2
	legs = (opposite ** 2) + (adjacent ** 2)
	if legs == hypotenuse:
		print("Right Triangle: "+str(True))
	else:
		print("Right Triangle: "+str(False))
	
def boolAcuteTriangle(opposite,adjacent,hypotenuse):
	hypotenuse = hypotenuse **2
	legs = (opposite ** 2) + (adjacent ** 2)
	if legs > hypotenuse:
		print("Acute Triangle: "+str(True))
	else:
		print("Acute Triangle: "+str(False))

def boolObtuseTriangle(opposite,adjacent,hypotenuse):
	hypotenuse = hypotenuse **2
	legs = (opposite ** 2) + (adjacent ** 2)
	if legs < hypotenuse:
		print("Obtuse Triangle: "+str(True))
	else:
		print("Obtuse Triangle: "+str(False))

def boolemailVerify(email):

	if str(".com") in email and str("@gmail") in email and str("@yahoo.com"):
		if str(" ") in email:
			print("Email Valid: "+str(False))
		else:
			print("Email Valid: "+str(True))
	else:
		print("Email Valid: "+str(False))




boolLess(2,4)
boolGreater(2,4)
boolInt(45)
boolFloat(3.5)
boolStr("Hi")
boolVerify(True)
boolListVerify(tuple((1,2,3,4,5)))
boolTupleVerify(tuple((1,2,3,4,5)))
boolSetVerify(set((1,2,3,4,5)))
boolDictionaryVerify(dict(num1= 2,num2=3))
boolIntList(list((1,2.3,2)))
boolFloatList(list((1.2,5,4.5,45)))
boolStrList(list(("Hello", 0,"Hi")))
boolOdd(3)
boolEven(5)
boolRightTriangle(3,4,5)
boolAcuteTriangle(5,6,10)
boolObtuseTriangle(5,10,14)
boolemailVerify("doradomiguel35@gmail.com")