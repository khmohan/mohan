class parent:
	def fun1(self):
		print("this is parent class")
class child(parent):
	def fun2(self):
		print("this is child class")
c=child()
c.fun1()
c.fun2()
