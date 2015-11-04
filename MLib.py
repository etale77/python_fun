#Returns [q,r] where a=bq+r and 0<=r<|b|. b cannot be 0
def euc_div(a,b): 
	if a==0:
		return [0,0]

	A = abs(a)
	B = abs(b)

	sgn_a = int(a/A)
	sgn_b = int(b/B)
	
	r = A%B
	q=int((A-r)/B)

	#Now the cases to deal with possible signs of a and b
	if sgn_a == sgn_b:
		if sgn_a > 0:
			return [q,r]
		return [q+1,B-r]
	if sgn_a > 0:
		return [-q,r]
	return [-q-1,B-r]

#Finds the corresponding remainder 0<=r<|b| of a/b
#The typical % operation is not sufficient for negative
#divisors in number theory applications
def modd(a,b):
	return euc_div(a,b)[1]

#Returns the sequence of divisors/remainders associated 
#with the Euclidean Algorithm. There are of the form 
#[[q(N+1),qN,...,q0][0,rN,r(N-1),...,r0]]
def euc_alg(a,b):
	div=euc_div(a,b)

	if div[1]==0:
		return [[div[0]],[0]]

	E=euc_alg(b,div[1])

	return [E[0]+[div[0]],E[1]+[div[1]]]



#return [x,y] so that ax+by=gdc(a,b)
def ext_euc_alg(a,b):
    if a == 0:
        return [0, 1]
    
    [y, x] = ext_euc_alg(b%a, a)
    return [x - int(b/a) * y, y]

def gcd(a,b):
	E=ext_euc_alg(a,b)
	return a*E[0]+b*E[1]

#Returns an N<pq so that N=a mod p and N=b mod q. It is assumed that p and q 
#are coprime
def crt(a,b,p,q):
	X=ext_euc_alg(p,q)
	return ((b*X[0]*p)+(a*X[1]*q))%(p*q)

#Checks if prime
def isprime(n):
	if n == 2 or n == 3: 
		return 1
	if n < 2 or n%2 == 0: 
		return 0
	if n < 9:
		return 1
	if n%3 == 0:
		return 0
	r = int(n**0.5)
	f = 5

	while f<=r:
		if n%f == 0:
			return 0
		if n%(f+2)==0:
			return 0
		f=f+6

	return 1

#Find the multiplicative inverse of x mod m
def inv_mod(x,m):
	C=ext_euc_alg(x,m)
	if C[0]*x+C[1]*m != 1:
		print("No multiplicative inverse possible.")
		return 0
	print('Inverse of ', x,'mod ',m,' = ', C[0]%m)
	return C[0]%m

#find the multiplicative inverse of x more pq
def inv_mod_ext(x,p,q):
	
	if gcd(p,q)!=1:
		return inv_mod(x,p*q)

	y_p=inv_mod(x,p)
	y_q=inv_mod(x,q)

	return crt(y_p,y_q,p,q)

#Find a^x mod n, using squaring techniques
def mod_pow(a,x,n):
	if x==0:
		return 1
	if x==1:
		return modd(a,n)
	if x==2:
		return modd(a*a,n)

	X=euc_div(x,2)
	b=modd(a*a,n)

	return modd(mod_pow(a,X[1],n)*mod_pow(b,X[0],n),n)

#If (b,N)=1, find a/b mod N
def mod_div(a,b,N):
	if gcd(b,N)!= 1:
		print("Error, divisor not invertible.")
		return
	d=inv_mod(b,N)


	return (a*d)%N

#take a list of integers L and reduce all of them mod N
def modd_list(L,N):
	k=0
	a=len(L)

	while k<a:
		L[k]=modd(L[k],N)
		k=k+1
	return L

#Evaluate the Legendre Symbol (a/p) using Euler's Criterion
def euler_crit(a,p):
	P=int((p-1)/2)
	k=mod_pow(a,P,p)

	if k!= 1:
		return -1
	return 1


#Takes a number and returns it's squarefree part
def squarefree_part(d):
	A=2

	while A <= int(abs(d)**(0.5)):

		while modd(d,A) != 0:
			A=A+1

		while modd(d,A*A) == 0:
			d=int(d/A)

		A=A+1

	return d

#Finds the Fundamental Discriminant of d
def fund_disc(d):
	d=squarefree_part(d)

	if d%4 != 1:
		d=4*d
	return d




































