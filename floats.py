import math

def floatAdd(a,b):
	result = float(a)+float(b)
	print(result)

def floatSub(a,b):
	result = float(a) - float(b)
	print(result)

def floatDivide(a,b):
	result = float(a) / float(b)
	print(result)

def floatMult(a,b):
	result = float(a) * float(b)
	print(result)

def floatFloor(a,b):
	result = float(a) // float(b)
	print(result)

def floatExponent(a,b):
	result = float(a) ** float(b)
	print(result)

def floatModulo(a,b):
	result = float(a) % float(b)
	print(result)

def floatSpeed(a,b,c):
	for x in range(a,b,c):
		print(str(x)+" mph")

def floatPay(money,price):
	if float(money) >= float(price):
		change = float(money) - float(price)
		print("Product Bought!")
		print("Change: PHP %.2f" %change)
	else:
		print("Isufficient funds")

def floatMoneyConvert(peso,countryAvailable):
	if str(countryAvailable.upper()) == "USA":
		money = peso * 0.019
		print("PHP -> USA = $ "+str(float(money)))

	elif str(countryAvailable.upper()) == "JAPAN":
		money = peso * 2.14
		print("PHP -> JAPAN = YEN "+str(float(money)))

def floatVerify(array):
	for x in array:
		if str(type(x)) == "<class 'float'>":
			print(str(x)+" is a float")

def floatToInt(a):
	print(int(a))

def floatAveHeight(maxHeight):
	aveHeight = (float(maxHeight)/2)
	print(str(aveHeight)+" ft")

def floatDiameter(radius):
	diameter = 2 * radius
	print("%.2f" %diameter)

def floatDiamCircum(circumeference):
	diameter = circumeference/ math.pi
	print("%.2f" %diameter)

def floatDiamArea(area):
	diameter = math.sqrt(area/math.pi) * 2
	print("%.2f" %diameter)

def floatAreaTriangle(base,height):
	area = 1/2 *(float(base) * float(height))
	print("%.2f" %area)

def floatHeightTriangle(area,base):
	height = (area/base) * 2
	print("%.2f" %height)

def floatAreaParallelogram(base,height):
	area = base * height
	print("%.2f" %area)

def floatHeightParallelogram(area,base):
	height = area/base
	print("%.2f" %height)

floatAdd(5.3,6.5)
floatSub(5.3,6.2)
floatDivide(4.6,10.2)
floatMult(3.5,5.5)
floatFloor(2.5,6.5)
floatExponent(4.5,2)
floatModulo(2.5,6.8)
# floatSpeed(1,60,2)
floatPay(1000,790)
floatMoneyConvert(2000,"Japan")
floatVerify([1,1.5,2,2.67])
floatToInt(4.567)
floatAveHeight(7.5)
floatDiameter(5.56)
floatDiamCircum(6.96)
floatDiamArea(4.68)
floatAreaTriangle(5.6,6.8)
floatHeightTriangle(4.5,3.5)
floatAreaParallelogram(7.6,8.5)
floatHeightParallelogram(10.5,5.5)