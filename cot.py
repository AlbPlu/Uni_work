import math

def trig_cot(a):
	if math.tan(a) != 0:
		return (1/(math.tan(a)))
	else:
		return ("Undefined")

a = float(input("enter number: "))
print(trig_cot(a))
