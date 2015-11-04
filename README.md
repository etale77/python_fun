# python_fun
Trying out and exploring ideas in/to learn python



Summaries of what each does:

**BSD_Exp.py --**
Using an Explicit Formula for the L-Function of an Elliptic Curve, it appears that we can construct a Chebyshev-type function for each elliptic curve based off of the modular coefficient q+1-N_q (where N_q = # E mod q). This formula predicts that, asymptotically, the Chebyshev function should behave like rx + Z(x), where Z(x) is some function coming from the nontrivial zeros of the associated L-Function and r is the analytic rank (BSD => algebraic rank) of E. The Generalized Riemann Hypothesis implies that Z(x) = o(x^(1+epsilon)) for any epsilon > 0. This program is to explore whether or not it is o(x) as well. If it is, then the limit of Cheb(x)/x as x-> infty should be r, if not then there should be some error associated to the nontrivial zeros.

The real time consumer is calculating N_p when p is an odd prime. The Schoof Algorithm implies this can be done in O((log p)^4) time, but it is involved to implement (future project?). I use Euler's Criterion to find points and this has allowed me to do this computation for x=1,...,10001 in reasonable time. The values bounce around the algebraic rank, but nothing is conclusive enough to make a conjecture about Z(x).

**GoL.py** --
An implementation of the Game of Life. Relatively simple in nature. One choice I made, that others may have too (or it might have been a bad choice), is to have each cell on the board keep track of what it's neighbors are independent of what the neighbors change to within a turn. This is to allow the board to refresh simlutaneously.

An important thing learned is how to do continuous updates of a graphic.

**Conic.py and ConicRSA.py --**
Conic sections have a natural, algebraic group law on them that is kind of like an affine version of the projective group law on Elliptic Curves. (It has been said that Conics are a "Poor Man's Elliptic Curve"). This law is geometricall motivated and them Linear Algebraic Groups. If we look mod N, for odd N, the conic x^2-y^2 = 4 is naturally isomorphic to (Z/NZ)^x. Conics of the form C_d: x^2-dy^2=4 are called Pell Conics and are easy to work with. If (d/p)=1, then C_d mod p is cyclic of size p-1, if (d/p)=-1, then C_d mod p is cyclic of size p+1. So I thought it would be fun to implement the addition rule on conics mod N and recreate the mathematical side of the encryption/decryption process of the RSA Algorithm for any curve, not just C_1. In this RSA implementation, adding a point to itself repeatedly can be calulated in much the same way as exponetiation is calculated in the typical RSA, just with different group laws.

All of the encryption/decryption calculations seem to be fine, but there also appears to be a problem with the implementation of the addition rule, which I need to rework.

**MLib.py --**
Just me exploring some basic Number Theory type algorithms. Sometimes I prefer the ones I made because they work more like they would in the mathematical context rather than how they do in python naturally.


