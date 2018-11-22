def bool_Less(a,b):
	if a < b:
		print(True)
	else:
		print(False)

def bool_Greater(a,b):
	if a > b:
		print(True)
	else:
		print(False)

def bool_Equal(a,b):
	if a == b:
		print(True)
	else:
		print(False)

def bool_Int(num):
	if str(type(num)) == "<class 'int'>":
		print("Int: "+str(True))

	else:
		print("Int: "+str(False))

def bool_Float(num):
	if str(type(num)) == "<class 'float'>":
		print("Float: "+str(True))
	else:
		print("Float: "+str(False)) 

def bool_Str(string):
	if str(type(string)) == "<class 'str'>":
		print("Str: "+str(True))
	else:
		print("Str: "+str(False)) 

def bool_Verify(bool):
	if str(type(bool)) == "<class 'str'>":
		print("Bool: "+str(False))

	elif str(type(bool)) == "<class 'bool'>":
		print("Bool: "+str(True))
	else:
		print("Bool: "+str(False)) 

def bool_List_Verify(list):
	if str(type(list)) == "<class 'list'>":
		print("List: "+str(True))
	else:
		print("List: "+str(False)) 

def bool_Set_Verify(set):
	if str(type(set)) == "<class 'set'>":
		print("Set: "+str(True))
	else:
		print("Set: "+str(False)) 

def bool_Tuple_Verify(tuple):
	if str(type(tuple)) == "<class 'tuple'>":
		print("Tuple: "+str(True))
	else:
		print("Tuple: "+str(False)) 


def bool_Dictionary_Verify(dictionary):
	if str(type(dictionary)) == "<class 'dictionary'>":
		print("Dictionary: "+str(True))
	else:
		print("Dictionary: "+str(False)) 

def bool_Int_List(list):
	result = True
	for x in list:
		if str(x) != "<class 'int'>":
			result = False
			break
	print("List Pure Int: "+str(result))

def bool_Float_List(list):
	result = True
	for x in list:
		if str(x) != "<class 'float'>":
			result = False
			break
	print("List Pure Float: "+str(result))

def bool_Str_List(list):
	result = True
	for x in list:
		if str(x) != "<class 'str'>":
			result = False
			break
	print("List Pure Str: "+str(result))

def bool_Odd(num):
	if num % 2 != 0:
		print("Odd:"+str(True))
	else:
		print("Odd:"+str(False))

def bool_Even(num):
	if num % 2 == 0:
		print("Even"+str(True))
	else:
		print("Even"+str(False))

def bool_Right_Triangle(opposite,adjacent,hypotenuse):
	hypotenuse = hypotenuse **2
	legs = (opposite ** 2) + (adjacent ** 2)
	if legs == hypotenuse:
		print("Right Triangle: "+str(True))
	else:
		print("Right Triangle: "+str(False))
	
def bool_Acute_Triangle(opposite,adjacent,hypotenuse):
	hypotenuse = hypotenuse **2
	legs = (opposite ** 2) + (adjacent ** 2)
	if legs > hypotenuse:
		print("Acute Triangle: "+str(True))
	else:
		print("Acute Triangle: "+str(False))

def bool_Obtuse_Triangle(opposite,adjacent,hypotenuse):
	hypotenuse = hypotenuse **2
	legs = (opposite ** 2) + (adjacent ** 2)
	if legs < hypotenuse:
		print("Obtuse Triangle: "+str(True))
	else:
		print("Obtuse Triangle: "+str(False))

def bool_email_Verify(email):

	if str(".com") in email and str("@gmail") in email and str("@yahoo.com"):
		if str(" ") in email:
			print("Email Valid: "+str(False))
		else:
			print("Email Valid: "+str(True))
	else:
		print("Email Valid: "+str(False))



bool_Less(2,4)
bool_Greater(2,4)
bool_Equal(2,2)
bool_Int(45)
bool_Float(3.5)
bool_Str("Hi")
bool_Verify(True)
bool_List_Verify(tuple((1,2,3,4,5)))
bool_Tuple_Verify(tuple((1,2,3,4,5)))
bool_Set_Verify(set((1,2,3,4,5)))
bool_Dictionary_Verify(dict(num1= 2,num2=3))
bool_Int_List(list((1,2.3,2)))
bool_Float_List(list((1.2,5,4.5,45)))
bool_Str_List(list(("Hello", 0,"Hi")))
bool_Odd(3)
bool_Even(5)
bool_Right_Triangle(3,4,5)
bool_Acute_Triangle(5,6,10)
bool_Obtuse_Triangle(5,10,14)
bool_email_Verify("doradomiguel35@gmail.com")