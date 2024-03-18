class mother:
	mothername=" "
	def fun1(self):
		print(self.mothername)
class father:
	fathername=" "
	def fun2(self):
		print(self.fathername)
class son(mother,father):
	def parents(self):
		print(self.fathername)
		print(self.mothername)
s=son()
s.mothername="sitha"
s.fathername="ram"
s.parents()
