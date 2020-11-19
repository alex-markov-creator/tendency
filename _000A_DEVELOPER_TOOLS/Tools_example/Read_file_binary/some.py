import pkgutil
data = pkgutil.get_data('some', 'text.txt')
print(data)