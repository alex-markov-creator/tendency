# Метод __getattr__ выполняет операцию получения ссылки на атрибут. Если говорить
# более определенно, он вызывается с именем атрибута в виде строки всякий
# раз, когда обнаруживается попытка получить ссылку на неопределенный (несуществующий) атрибут.
class empty:
	def __getattr__(self, attrname):
		if attrname == 'age':
			return 40
		else:
			raise AttributeError ('attrname')

X = empty()
print(X.age)
print(X.name)