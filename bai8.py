def isTriangle(a:int,b:int,c:int):
	c = [a,b,c]
	c.sort()
	if c[0] + c[1] > c[2]:
		return True
	else:
		return False

a,b,c = map(int, input().split())

p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))**0.5
if isTriangle(a,b,c):
	print(f'{a*b*c/(4*s):.3f}')
else:
	print("Deo")

