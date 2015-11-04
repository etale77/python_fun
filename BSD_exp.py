import math
import MLib

#This class of Elliptic Curves will store a curve y^2=x^3+ax+b as [a,b].
#Also, whenever a size or modular coefficient is computed it will be stored along with
#the size of the field it was found in.
#Sizes of the curve mod p are computed using Euler's Criterion. Schoof's Algorithm is better but much more involved
class elliptic_curve:
	#saves the curve as y^2=x^3+ax+b
	def __init__(self, a,b):
		self.coef = [a,b]
		self.sizes = []
		self.mod_coeff = []

	def size_modp(self, p):
		
		#If we already know this size, return it from the saved list.
		if len(self.sizes)>0:
			for n in range(len(self.sizes)):
				if self.sizes[n][1]==p:
					return self.sizes[n][0]

		#Computes the size mod 2
		N = 1
		if p==2:
			for x in range(2):
				for y in range(2):
					if (y**2-((x**3) +self.coef[0]*x +self.coef[1]))%2 ==0:
						N=N+1
			self.sizes.append([N,p])
			return N

		#If we don't know the size of E mod p where p is odd, then we use Euler's Criterion to check
		#if x^3+ax+b is a square mod p or not.
		for x in range(p):
			X=(x**3) +self.coef[0]*x +self.coef[1]
			L=MLib.euler_crit(X,p)
			if  L== 1 :
				N=N+2
			if L==0:
				N=N+2
			if N > p+3 +2*int(p**(0.5)):
					break
		self.sizes.append([N,p])
		print(p,N," : ", N-(p+1), 2*(p**(0.5))) #For visual progress reports while running.
		return N


	#Determines a modular coefficient associated to a prime.
	def mod_coeffp(self, p):
		if len(self.mod_coeff)>0:
			for n in range(len(self.mod_coeff)):
				if self.mod_coeff[n][1]==p:
					return self.mod_coeff[n][0]

		N = self.size_modp(p)
		a = p+1 - N
		self.mod_coeff.append([a,p])
		return a

	#Determines the modular coefficient associated to q=p^n
	def mod_coeffq(self,p,n):
		if len(self.mod_coeff)>0:
			for k in range(len(self.mod_coeff)):
				if self.mod_coeff[k][1]==p**n:
					return self.mod_coeff[k][0]


		a = self.mod_coeffp(p)
		c=2
		if n==1:
			return a
		if n==2:
			self.mod_coeff.append([(a**2)-c*p,p**2])
			return (a**2)-c*p
		if n>2:
			b=a*self.mod_coeffq(p,n-1)-p*self.mod_coeffq(p,n-2)
			self.mod_coeff.append([b,p**n])
			return b

#Simple sieve of Ero
def seive(K):
	L=[1 for n in range(K+1)]

	L[0]=0
	L[1]=0
	for n in range(2,int((K+1)**(0.5)+2)):
		if L[n] == 1:
			m=n**2
			while m <= K:
				L[m]=0
				m=m+n
	
	P=[]
	for n in range(len(L)):
		if L[n]==1:
			P.append(n)
	return P

#The definition of the Chebyshev-Type function which should asymptotically behave like rx
#where r is the analytic rank of E (BSD => r is the rank of E). 
#There may or may not be a nontrivial error to this approximamtion. This code is to see if it is big or not. 
def cheb_E(E,x,P):
	C=0
	
	for p in P:
		if p>x:
			break

		m=1
		L=math.log(p)
		while p**m <= x:
			C=C-E.mod_coeffq(p,m)*L
			m=m+1
	return C

		



P=seive(1000000)
E = elliptic_curve(-52,145)

#runs through the Chebyshev values for x between 1 and whatever. It could be run faster by 
#incimenting rather than recalculating, but this wouldn't speed things up much because the elliptic curve
#itself stores this info. The biggest time-hog is computing the size of E mod p.
f = open('curve_-52_145.txt','w')
f.write('-52,145, Rank = 2 \n')
for x in range(1,10001):
	print(x,':',cheb_E(E,x,P)/x)
	f.write(str(x))
	f.write(':')
	f.write(str(cheb_E(E,x,P)/x))
	f.write('\n')






