class UF:
	def __init__(self, N):
		self.up_bound = list(range(N))
		self._count = N
		self.rank = [0]*N
	def find(self, x_index):
		if self.up_bound[x_index] == x_index:
			return x_index
		self.up_bound[x_index] = self.find(self.up_bound[x_index])
		return self.up_bound[x_index]
	def count(self):
		return self._count	
	def union(self, x_index, y_index):
		x = self.find(x_index)
		y = self.find(y_index)
		
		if x == y:
			return False
		if self.rank[x] == self.rank[y]:
			self.rank[x] += 1
			self.up_bound[y] = x
		elif self.rank[x] > self.rank[y]:
			self.up_bound[y] = x
		else:
			self.up_bound[x] = y
		return True
	def printSets(universe, ds):
		print([ds.Find(i) for i in universe])	
	def __str__(self):
		return " ".join([str(x) for x in self.up_bound])

	def __repr__(self):
		return "UF(" + str(self) + ")"
