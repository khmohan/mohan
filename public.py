class rvce:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def dispalyage(self):
		print("age:",self.age)
r=rvce("abc" ,20)
print("name:",r.name)
r.dispalyage()
