m,n = map(int,input().split())

def isNguyenTo(a:int):
	count = 0
	for i in range(1,a+1):
		if a%i == 0:
			count += 1
	if count >= 3:
		return False
	return True
count = 0
total = 0
for i in range(m,n+1):
	if isNguyenTo(i):
		total += i
		count += 1
print(f'{total/count:.2f}')