a = str(input())

total = 0

for i in a:
	total += int(i)

if total%10 ==9:
	print(total%10)
	print('may man')
else:
	print(total%10)
	print('chua may man')