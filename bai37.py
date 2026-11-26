a,b = map(int,input().split())

def ucln(a:int,b:int):
	if b == 0:
		return a
	return ucln(b,a%b)

print(f'{int(a/ucln(a,b))}/{int(b/ucln(a,b))}')