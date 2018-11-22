def bool_Less(a,b):
	if a < b:
		return True 
	else:
		return False

def bool_Greater(a,b):
	if a > b:
		return True
	else:
		return False

def bool_Equal(a,b):
	if a == b:
		return True
	else:
		return False

def bool_Int(num):
	if str(type(num)) == "<class 'int'>":
		return str("Int: "+str(True))

	else:
		return str("Int: "+str(False))

def bool_Float(num):
	if str(type(num)) == "<class 'float'>":
		return str("Float: "+str(True))
	else:
		return str("Float: "+str(False)) 

def bool_Str(string):
	if str(type(string)) == "<class 'str'>":
		return str("Str: "+str(True))
	else:
		return str("Str: "+str(False)) 

def bool_Verify(bool):
	if str(type(bool)) == "<class 'str'>":
		return str("Bool: "+str(False))

	elif str(type(bool)) == "<class 'bool'>":
		return str("Bool: "+str(True))
	else:
		return str("Bool: "+str(False)) 

def bool_List_Verify(list):
	if str(type(list)) == "<class 'list'>":
		return str("List: "+str(True))
	else:
		return str("List: "+str(False)) 

def bool_Set_Verify(set):
	if str(type(set)) == "<class 'set'>":
		return str("Set: "+str(True))
	else:
		return str("Set: "+str(False)) 

def bool_Tuple_Verify(tuple):
	if str(type(tuple)) == "<class 'tuple'>":
		return str("Tuple: "+str(True))
	else:
		return str("Tuple: "+str(False)) 


def bool_Dictionary_Verify(dictionary):
	if str(type(dictionary)) == "<class 'dictionary'>":
		return str("Dictionary: "+str(True))
	else:
		return str("Dictionary: "+str(False)) 

def bool_Int_List(list):
	result = True
	for x in list:
		if str(x) != "<class 'int'>":
			result = False
			break
	return str("List Pure Int: "+str(result))

def bool_Float_List(list):
	result = True
	for x in list:
		if str(x) != "<class 'float'>":
			result = False
			break
	return str("List Pure Float: "+str(result))

def bool_Str_List(list):
	result = True
	for x in list:
		if str(x) != "<class 'str'>":
			result = False
			break
	return str("List Pure Str: "+str(result))

def bool_Odd(num):
	if num % 2 != 0:
		return str("Odd:"+str(True))
	else:
		return str("Odd:"+str(False))

def bool_Even(num):
	if num % 2 == 0:
		return str("Even"+str(True))
	else:
		return str("Even"+str(False))

def bool_Right_Triangle(opposite,adjacent,hypotenuse):
	hypotenuse = hypotenuse **2
	legs = (opposite ** 2) + (adjacent ** 2)
	if legs == hypotenuse:
		return str("Right Triangle: "+str(True))
	else:
		return str("Right Triangle: "+str(False))
	
def bool_Acute_Triangle(opposite,adjacent,hypotenuse):
	hypotenuse = hypotenuse **2
	legs = (opposite ** 2) + (adjacent ** 2)
	if legs > hypotenuse:
		return str("Acute Triangle: "+str(True))
	else:
		return str("Acute Triangle: "+str(False))

def bool_Obtuse_Triangle(opposite,adjacent,hypotenuse):
	hypotenuse = hypotenuse **2
	legs = (opposite ** 2) + (adjacent ** 2)
	if legs < hypotenuse:
		return str("Obtuse Triangle: "+str(True))
	else:
		return str("Obtuse Triangle: "+str(False))

def bool_email_Verify(email):

	if str(".com") in email and str("@gmail") in email and str("@yahoo.com"):
		if str(" ") in email:
			return str("Email Valid: "+str(False))
		else:
			return str("Email Valid: "+str(True))
	else:
		return str("Email Valid: "+str(False))



print(bool_Less(2,4))
print(bool_Greater(2,4))
print(bool_Equal(2,2))
print(bool_Int(45))
print(bool_Float(3.5))
print(bool_Str("Hi"))
print(bool_Verify(True))
print(bool_List_Verify(tuple((1,2,3,4,5))))
print(bool_Tuple_Verify(tuple((1,2,3,4,5))))
print(bool_Set_Verify(set((1,2,3,4,5))))
print(bool_Dictionary_Verify(dict(num1= 2,num2=3)))
print(bool_Int_List(list((1,2.3,2))))
print(bool_Float_List(list((1.2,5,4.5,45))))
print(bool_Str_List(list(("Hello", 0,"Hi"))))
print(bool_Odd(3))
print(bool_Even(5))
print(bool_Right_Triangle(3,4,5))
print(bool_Acute_Triangle(5,6,10))
print(bool_Obtuse_Triangle(5,10,14))
print(bool_email_Verify("doradomiguel35@gmail.com"))