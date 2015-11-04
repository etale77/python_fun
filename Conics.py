import MLib

#Given a discriminant D, this code will compute on the arithmetic
#of the Pell Conic with this discriminant (x^2-Dy^2=4), mod N with basepoint
#(2,0)

#From here on D represents the discriminant and N>0 is the number we are
#working under. A conice will equal [D,N].

#Determines if the point P=[x,y] is on Pell_D mod N
def is_on(P,C):
	V = (P[0]*P[0]-C[0]*P[1]*P[1]-4)%C[1]
	
	if V==0:
		return 1
	return 0

#Given a pair of points, P in (Z/nZ)^2 and Q in (Z/mZ)^2
#with gcd(n,m) assumed to be 1, this finds a point in (Z/mnZ)^2
#that reduces to these two points
def crt2(P,Q,n,m):
	return [MLib.crt(P[0],Q[0],n,m),MLib.crt(P[1],Q[1],n,m)]

#Given two points, return the line L[0]x+L[1]y+L[2]=0 that 
#goes through P and Q. We must be able to account for P==Q
#in which case we return the tangent line of the conic at that point
#also reduces mod N
def line(P,Q,C):
	N=C[1]
	if P==Q:
		dx=C[0]*P[1]
		dy=P[0]
		c=-dx*P[1]+dy*P[0]

		return [(-dy)%N,dx%N,c%N]

	dx=P[0]-Q[0]
	dy=P[1]-Q[1]
	g=MLib.gcd(dx,dy)

	a=int(dy/g)
	b=-int(dx/g)
	c=-P[0]*dy+P[1]*dx

	
	return [a%N,b%N,c%N]

#Given a line L, find the line parallel to L through O=(2,0)
#all while reducing the coefficients mod N
def par_line(L,C):
	if (2*L[0]+L[2])%C[1]==0:
		return L
	return [L[0],L[1],(-2*L[0])%C[1]]

#Given two points on the conic C=[D,N], find their Conic Sum
#with respect to the origin (2,0)
#In this case, the formula is simplified and faster than in the
#general case (which I also have written)
def conic_add(P,Q,C):
	x=MLib.mod_div(P[0]*Q[0]+C[0]*P[1]*Q[1],2,C[1])
	y=MLib.mod_div(P[0]*Q[1]+P[1]*Q[0],2,C[1])


	return [x,y]


#Given a point P on C, multiply it by k
#This uses the same efficient algorithm as large exponentiation
#as the processes are the same
def mult_pt(P,C,k):
	if k==0:
		return [2,0]
	if k==1:
		return P
	if k==2:
		return conic_add(P,P,C)

	X=MLib.euc_div(k,2)
	Q=conic_add(P,P,C)

	return conic_add(mult_pt(P,C,X[1]),mult_pt(Q,C,X[0]),C)

#Given a conic C=[D,p] where p is prime, find the number of points
#Makes heavy use of Legendre Symboles and Euler's Criterion
def conic_size(C):
	return C[1]-MLib.euler_crit(C[0],C[1])

#Find the inverse of "Multiplication by k" in the conic [D,pq]
#given  C=[D,p] and B=[D,q]
def conic_inv(k,C,B):
	a=conic_size(C)
	b=conic_size(B)

	return MLib.inv_mod_ext(k,a,b)

#Uses brute force to find the order of P on C
def brute_find_ord(P,C):
	Q=P
	k=0

	while Q[0]!=2 and Q[1]!= 0:
		Q=conic_add(P,Q,C)
		k=k+1

	return k





