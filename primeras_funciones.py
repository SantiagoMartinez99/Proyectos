def pot(n,m):
	if n==0: 
		return n
	if m==0:
		return 1
	return pot(n,m-1)*n

def fibo(numero):
	if numero<2:
		return 1
	return fibo(numero-1)+fibo(numero-2)

def division(a,b):
	if b>a:
		return "El resultado es 0"
	return division((a-b)*b)+1

print(fibo(4))
print(pot(5,2))
print(division(10,5))