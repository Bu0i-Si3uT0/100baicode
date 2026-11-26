a,b = map(int, input().split())

def ucln(m:int,n:int):
	if n == 0:
		return m
	return ucln(n,m%n)

print(ucln(a,b))