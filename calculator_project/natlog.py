import math

def nat_log(a):
	if a<=0:
		return ("logarithms are undefined for non-positive numbers")
	else:
		return math.log(a)

a = float(input("enter number: "))
print(nat_log(a))
