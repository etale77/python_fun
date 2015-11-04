import time
import numpy as np
import matplotlib.pyplot as plt

class GoL:
	def __init__(self,N,M):
		self.board = [[[0,[0 for x in range(8)]] for x in range(M+2)] for x in range(N+2)]
		self.rows=N
		self.cols=M
		#A cell in the board is of the form [0,[0,1,0,0,1,0,1,1]]
		#where the second list is the list of statuses of it's neighbors
		#where the index can be visualized by
		#  012
		#  7 3
		#  654
	
	#Changing the status of a single cell based on it's neighbor's statuses
	def iterate_cell(self, a,b):
		
		#First count how many alive neigbors the point has
		s=0
		for k in range(8):
			s=s+self.board[a][b][1][k] #This iterates around the neighbor statuses and adds them up

		#If changes need to be made, this will do it.
		if self.board[a][b][0] == 1:
			if s!=2 and s!=3:
				self.board[a][b][0]=0
		if self.board[a][b][0] ==0:
			if s==3:
				self.board[a][b][0]=1
	
	#After a change has been made, the neighbors must be adjusted so that they are up-to-date
	def update_nb(self):
		n=1
		m=1
		while n<=self.rows:
			while m<=self.cols:
				self.board[n][m][1][0] = self.board[n-1][m-1][0]
				self.board[n][m][1][1] = self.board[n][m-1][0]
				self.board[n][m][1][2] = self.board[n+1][m-1][0]
				self.board[n][m][1][3] = self.board[n+1][m][0]
				self.board[n][m][1][4] = self.board[n+1][m+1][0]
				self.board[n][m][1][5] = self.board[n][m+1][0]
				self.board[n][m][1][6] = self.board[n-1][m+1][0]
				self.board[n][m][1][7] = self.board[n-1][m][0]
				m=m+1
			n=n+1
			m=1

	#Iterate the entire board, and updating the neighbor info
	def iterate(self):
		n=1
		m=1

		while n<=self.rows:
			while m<=self.cols:
				self.iterate_cell(n,m)
				m=m+1
			n=n+1
			m=1
		self.update_nb()

	#Print the board, if we need to
	def print_board(self):
		m=1

		while m<=self.cols:
			print([self.board[n+1][m][0] for n in range(self.rows)])
			m=m+1

	#For a list of with elements of the form [n,m,x], change the value of the (n,m) cell to x
	def set_pts(self, L):
		for k in range(len(L)):
			self.board[L[k][0]][L[k][1]][0] = L[k][2]
		self.update_nb()

#Play a game with random initial conditions.
def play_rand(N,M):
	game=GoL(N,M)
	L=[]

	x=1
	for n in range(N):
		for m in range(M):
			k=np.random.random_integers(0,1)
			x=x+1
			if k==1:
				L=L+[[n,m,1]]
			if x%5000==0:
				print(x)

	game.set_pts(L)

	array=np.array([[game.board[n+1][m+1][0] for n in range(N)] for m in range(M)])
	im=plt.imshow(array, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 1,interpolation="nearest")
	
	plt.ion()
	plt.show()

	for i in range(1000):
		game.iterate()
		array= np.array([[game.board[n+1][m+1][0] for n in range(N)] for m in range(M)])
		
		im=plt.imshow(array, cmap = plt.get_cmap('gray'), vmin = 0, vmax = 1,interpolation="nearest")
		plt.pause(0.001)
		plt.cla()



play_rand(50,50)