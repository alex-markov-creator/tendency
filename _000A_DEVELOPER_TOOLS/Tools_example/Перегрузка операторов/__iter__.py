class Squares:
	def __init__(self, start, stop): # Сохранить состояние при создании
		self.value = start - 1
		self.stop = stop

	def __iter__(self): # Возвращает итератор в iter()
		return self

	def __next__(self):	# Возвращает квадрат в каждой итерации  
		if self.value == self.stop:	# Также вызывается функцией next
			raise StopIteration
		self.value += 1
		return self.value ** 2

for i in Squares(1, 5):	# for вызывает iter(), который вызывет __iter__()
	print(i, end=' ')	# на каждой итерции вызывается __next__()

