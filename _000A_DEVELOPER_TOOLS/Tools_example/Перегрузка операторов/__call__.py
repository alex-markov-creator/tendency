class Callee:
	def __call__(self, *pargs, **kargs): # релизует вызов экземпляра
		print('Called:', pargs, kargs) # принимает любые аргументы

c = Callee()
c(1,2,3)