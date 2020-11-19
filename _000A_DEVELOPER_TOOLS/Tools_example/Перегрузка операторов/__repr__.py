class adder:
	def __init__(self, value=0):
		self.data = value	# Инициализировать атрибут data
	
	def __add__(self, other):	# Прибавить другое значение
		self.data += other

class addrepr(adder):	# Наследует __init__, __add__
	def __repr__(self):	# Добавляет строковое представление
		return 'addrepr(%s)' % self.data	# Преобразует в строку программного кода

x = addrepr(2)	# Вызовет __init__
x+1	# Вызовет __add__
print(x)	# Вызовет __repr__
