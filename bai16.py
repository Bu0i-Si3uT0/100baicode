a,b = map(float,input().split())

tb = (a+b*2)/3

if tb >= 8:
	print(f'{tb:.1f}')	
	print('Gioi')
elif 6.5 <= tb:
	print(f'{tb:.1f}')
	print('Kha')
elif tb >= 5:
	print(f'{tb:.1f}')
	print('Trung binh')
elif tb >= 3.5:
	print(f'{tb:.1f}')
	print('Yeu')
else:
	print(f'{tb:.1f}')
	print('Kem')