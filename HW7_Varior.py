from random import randint
a = [randint(1,20) for i in range(0,31)]
b = [randint(1,20) for i in range(0,31)]
c = [randint(1,20) for i in range(0,31)]
x = 1
y = 1
z = 1

def cacl(a, b, c, x, y, z):
	for i in range(0,31):
		k += a[i]*(x**(30-i))
		l += b[i]*(x**(30-i))
		m += c[i]*((x+z)**(30-i))
	return (k**2-l)/m

#-------------------------------------

m = 5
n = 3

def factorial(x):
	if x == 0:
		return 1
	else:
		return x*factorial(x-1)

def F(m, n):
	return (factorial(n)*factorial(m))/factorial(n+m)

#---------------------------------------------------

def Perestanovka(x,y):
	if len(x)=len(y):
		y1 = y
		for i in x:
			if y1.find(i) != -1:
				y1 = y1.replace(i, '')
			else:
				return "not possible"
	else:
		return "not possible"
	return x
				
#---------------------------------

a = []
b = []

def maxmatrix(a, b):
	maxa = 0
	maxb = 0
	cora = []
	corb = []
	for i in range(len(a)):
		for j in range(len(i)):
			if a[i,j] > maxa
			maxa = a[i,j]
			cora = [i,j]
	for i in range(len(b)):
		for j in range(len(i)):
			if b[i,j] > maxb
			maxb = b[i,j]
			corb = [i,j]
	a[cora[0], cora[1]] = maxb
	b[corb[0], corb[1]] = maxa
	for l in range(1,6):
		print (a[l]+"      "+b[l]+"\n")


#----------------------------

def mysort(x):
	n = len(x)
	while n > = 1:
		for i in range(n-1):
			if x[i]<x[i+1]
			x[i], x[i+1] = x[i+1], x[i]
		n -= 1