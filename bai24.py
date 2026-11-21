n = int(input())

if n%3 == 0:
	print(int((n-3)/3+1))
elif n%3 == 1:
	print(int((n-1-3)/3+1))
else:
	print((n-2-3)/3+1)