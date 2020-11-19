class Indexer:
	def __getitem__(self, index):
		return index ** 2

X = Indexer()
print(X[2])	# Выражение X[i] вызывает X.__getitem__(i)

for i in range(10):
	print(X[i], end=' ') # Вызывает __getitem__(X, i) в каждой итерации
