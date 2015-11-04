import MLib
import Conics

#Conoic sections are affine groups under a geometric addition rule
#similar to Elliptic Curves, but with no need for a point at infinity.
#Pell Conics are the special conics of the form x^2-dy^2=4. Each
#conic is isomorphic to a Pell Conic of the same discriminant.
#For instance the curve xy=1, when taken mod N, corresponds to 
#the multiplicative group mod N and is isomorphic to the Pell Conic
#x^2-y^2=4 where (x,y) on the Pell Conic corresponds to ((x-y)/2,(x+y)/2)
#when we mod by an odd N.
#We can then use the ideas of the typical RSA Encryption to encrypt 
#a point on a Pell Conic and use knowledge of the conic and of the
#prime factorization of N=pq to find a private key quickly via the
#Chinese Remainder Theorem. This is what this program does


#Setup: Specify the discriminant of the Pell Conic. Specify N=pq,
#N is public and p,q are private. Choose a code ie an integer
#e to encode the points. Use the Chinese Remainder Theoerem to
#find the inverse k of e for this curve.

print('--Initialize the Curve--')
print('-The curve will be the Pell Conic x^2-dy^2=4 mod N=pq')
d = MLib.fund_disc(int(input('Input the Discriminant d:')))


p = int(input('Input the first prime factor of N: '))
while MLib.isprime(p)==0:
	p = int(input('That was not prime, please input a prime: '))



q = int(input('Input the second prime factor of N: '))
while MLib.isprime(q)==0:
	q = int(input('That was not prime, please input a prime: '))
	while p==q:
		q = int(input('That number will not work, try another: '))
	
N=p*q
C=[d,N]
A=[d,p]
B=[d,q]

r=Conics.conic_size(A) #Size of C mod p
s=Conics.conic_size(B)	#Size of C mod q
M=r*s #Size of C mod N (due to CRT)



#Input key
e = int(input('Input the Public Key: '))
while MLib.gcd(e,M)!=1:
	e = int(input('That key will not do, try another: '))

#Output reverse key
k = Conics.conic_inv(e,A,B)

print('')
print('--Public Information--')
print('The Conic: x^2 -', d,'y^2 = 4')
print('The Modular Number: ', N)
print('The Key: ', e)
print('')
print('--Private Information--')
print('The Factorization: ', N,'=', p,'*', q)
print('The Size of the Conic: ', M,'=', r,'*',s)
print('The Reverse Key: ', k)
print('')

choice=1
while choice==1:
	#Point to encode
	a = int(input('Type the x-value of the point to encode: '))
	b = int(input('Type the y-value of the point to encode: '))
	
	P=[a,b]

	on=Conics.is_on(P,C)
	
	while on == 0:
		print('That point is not on the curve. Try again.')
		a = int(input('Type the x-value of the point to encode: '))
		b = int(input('Type the y-value of the point to encode: '))
	
		P=[a,b]

		on=Conics.is_on(P,C)

	

	Q = Conics.mult_pt(P,C,e)
	print('')
	print('Encoded point: ', Q)
	print('')
	print("Decoding...")
	print(Conics.mult_pt(Q,C,k))
	print('')


	choice = int(input('Encode another point? '))