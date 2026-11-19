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
	print("Day la 3 canh cua mot tam giac")
	print(f'{a+b+c:.2f} {s:.1f}')
else:
	print("Day khong phai la 3 canh cua mot tam giac")

