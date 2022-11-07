import random
import matplotlib.pyplot as plt
import sys

class RW:

	def __init__(self,n,N):
		self.N = N
		self.n = n
		self.rw = self.list_of_dim()
				
		
	def list_of_dim(self):
		rw =[0]*self.n
		for i in range (self.n):
			rw[i] = [0]*self.N
		return rw
		
	
	def fill(self):
		for i in range (self.N-1):
			dimchange = random.randint(0, self.n-1)
			for j in range(self.n):
				if j != dimchange:
					self.step_1(j,i)
				else:
					self.step_2(j,i)
		return self.rw
	
	
	def step_1(self,j,i):
		self.rw[j][i+1] = self.rw[j][i]
		return
	
	def step_2(self, j, i):
		dice = random.random()
		if dice > 0.5:
			self.rw[j][i+1] = self.rw[j][i]+1
		else:
			self.rw[j][i+1] = self.rw[j][i]-1
		return
	
	def display(self):
		if self.n == 1:
			plt.plot(list(range (self.N)), self.rw[0])
			plt.show()
		elif self.n == 2:
			plt.plot(self.rw[0],self.rw[1])
			plt.show()
		elif self.n == 3:
			m = plt.subplot(111,projection = "3d")
			m.plot(self.rw[0], self.rw[1], self.rw[2])
			plt.show()
		elif self.n>3:	
			for i in range(self.n):
				print("din" , i+1, end = ": [ ")
				for j in range(self.N):
					print(self.rw[i][j], end = ", ")
				print("]")		
		return
					

random_walk = RW(int(sys.argv[1]), int(sys.argv[2]))
random_walk.fill()
random_walk.display()
