import math
import MLib

class elliptic_curve:

	#saves the curve as y^2=x^3+ax+b
	def __init__(self, a,b):
		self.coef = [a,b]
		self.sizes = []
		self.mod_coeff = []

	def size_modp(self, p):
		if len(self.sizes)>0:
			for n in range(len(self.sizes)):
				if self.sizes[n][1]==p:
					return self.sizes[n][0]

		N = 1

		if p==2:
			for x in range(2):
				for y in range(2):
					if (y**2-((x**3) +self.coef[0]*x +self.coef[1]))%2 ==0:
						N=N+1
			self.sizes.append([N,p])
			return N

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
		print(N,p," : ", N-(p+1), 2*(p**(0.5)))
		return N



	def mod_coeffp(self, p):
		if len(self.mod_coeff)>0:
			for n in range(len(self.mod_coeff)):
				if self.mod_coeff[n][1]==p:
					return self.mod_coeff[n][0]

		N = self.size_modp(p)
		a = p+1 - N
		self.mod_coeff.append([a,p])
		return a

	#q=p^n
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


f = open('curve_-52_145.txt','w')
f.write('-52,145, Rank = 2 \n')
for x in range(1,10001):
	print(x,':',cheb_E(E,x,P)/x)
	f.write(str(x))
	f.write(':')
	f.write(str(cheb_E(E,x,P)/x))
	f.write('\n')






