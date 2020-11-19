#-*- coding: utf-8 -*-

# @author 

##############################
# СТРУКТУРЫ ДАННЫХ И АЛГОРИТМЫ
##############################

"""
# 1.1
# Распаковка последовательности в отдельные переменные
######################################################

data = ['ACME', 58, 98.1, (2012, 12, 21)]
name, share, price, date = data
print(name, date)

# Отбраковка некоторых значений
###############################
data_copy = ['ACME', 58, 98.1, (2012, 12,21)]
_, share, price, _ = data_copy
print(share, price)
"""

"""
#1.2 
# Распаковка элементов из последовательностей произвольной длины
################################################################

# В конце семестра вы решаете,
# что не будете принимать во внимание оценки за первое и последнее домашние
# задания, а по остальным оценкам посчитаете среднее значение. Если у вас было
# четыре задания, то можно просто распаковать все четыре. Но что делать, если их
# 24? Выражение со звездочкой позволит легко решить эту задачу:

grades = [2,4,5,2,3,4,5,3]

def avg(middle):
	sum = 0
	for i in middle:
		sum += i
	return sum/len(middle)

def drop_first_last(grades):
	first, *middle, last = grades
	return avg(middle)
	

print(drop_first_last(grades))

# Второй пример
###############
record = ('Dave', 'dave@example.com', '773-443-6657', '456-456-765-4564')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers) 

# Есть последовательность значений, 
# представляющая продажи вашей компании 
# за последние восемь кварталов. 
# Необходимо посмотреть, как последний квартал 
# соотносится со средним значением по первым семи

def avg(sales_record):
	*trailing_qtrs, current_qtr = sales_record
	trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
	return print(trailing_avg, current_qtr)

avg([10,8,7,1,9,5,10,3])


# ОБСУЖДЕНИЕ
############
# Синтаксис звездочки особенно полезен  при итерировании 
# по последовательности кортежей переменной длины

records = [
	('foo', 1, 2),
	('bar', 'hello'),
	('foo', 3, 4),
]

def do_foo(x,y):
	print('foo', x, y)

def do_bar(s):
	print('bar', s)

for tag, *args in records:
	if tag == 'foo':
		do_foo(*args)
	elif tag == 'bar':
		do_bar(*args)

# Распаковка со звездочкой также может быть полезна 
# в комбинации с операциями обработки строк, такими как разрезание
###################################################################
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# Иногда вам может быть нужно распаковать значения и отбросить их. 
# Вы не можете просто определить голую * при распаковке, но можно использовать обычное
# для отбрасывания имя переменной, такое как _ или ign (ignored). 
###############################################################################
record = ('ACME', 58, 98.1, (2012, 12,21))
name, *_, (*_, year) = record
print(name)
print(year)

# Функция, которая произведет разрезание спомощью хитрого рекурсивного алгоритма 
###############################################################################
items = [1, 10, 7, 4, 5, 9]
def sum(items):
	head, *tail = items
	return head + sum(tail) if tail else head
print(sum(items))
"""

"""

#1.3
# Оставляем N последних элементов
#################################
# Задача хранения ограниченной истории – отличный повод применить collections.
# deque. Например, следующий фрагмент кода производит простое сопоставление
# текста с последовательностью строк, а при совпадении выдает совпавшие строки
# вместе с N предыдущими строками контекста:
from collections import deque
def search(lines, pattern, hystory=5):
	previous_lines = deque(maxlen=hystory)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)

if __name__ == '__main__':
	with open('somefile.txt') as f:
		for line, prevlines in search(f, 'Hello_test', 3):
			for pline in prevlines:
				print(pline, end=' ')
			print(line, end=' ')
			print('-'*20)
"""

"""
# Обсуждение
############
# Использование deque(maxlen=N) создает очередь фиксированной длины. Когда
# новые элементы добавлены и очередь заполнена, самый старый элемент автома-
# тически удаляется. Пример:
from collections import deque
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
"""

"""
# 1.4
# Поиск N максимальных и минимальных элементов
##############################################
# Создать список N максимальных или минимальных элементов коллекции
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Выведет [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Выведет [-4, 1, 2]

# Обе функции также принимают параметр key, который позволяет использовать
# их с более сложными структурами данных. Например:
portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)
# ОБСУЖДЕНИЕ
############
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
"""

"""
# 1.5
# Реализация очереди с приоритетом
##################################
# Реализовать очередь, которая сортирует элементы по заданному приоритету
# и всегда возвращает элемент с наивысшим приоритетом при каждой операции 
# получения (удаления) элемента.
import heapq
class PriorityQueue:
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)[-1]

class Item():
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
"""	


# 1.6
# Отображение ключей на несколько значений в словаре
####################################################
# Вы хотите создать словарь, который отображает ключи на более чем одно значе-
# ние (так называемый «мультисловарь», multidict).
"""
d = {
	'a': [1, 2, 3],
	'b': [4, 5]
}
e = {
	'a' : {1, 2, 3},
	'b' : {4, 5}
}
# Чтобы легко создавать такие словари, вы можете использовать defaultdict из
# модуля collections. Особенность defautdict заключается в автоматической инициализации
# первого значения, так что вы можете сосредоточиться на добавлении
# элементов.
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)
# Обсуждение
# Конструирование словарей со множественными значениями не является чем-то
# сложным. Однако инициализация первого значения может быть запутанной, если
# вы пытаетесь сделать это самостоятельно.
d = {}
for key, value in pairs:
	if key not in d:
		d[key] = []
	d[key].append(value)

d = defaultdict(list)
for key, value in pairs:
	d[key].append(value)
"""

"""
# 1.7
# Поддержание порядка в словарях
################################
# Вы хотите создать словарь, который позволит контролировать порядок элементов
# при итерировании по нему или при сериализации.
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
	print(key, d[key])
import json
print(json.dumps(d))

# Обсуждение
# OrderedDict внутри себя поддерживает двусвязный список, который упорядочи-
# вает ключи в соответствии с порядком добавления. Когда новый элемент встав-
# ляется впервые, он помещается в конец этого списка. Последующее связывание
# значения с существующим ключом не изменяет порядок.
# Заметьте, что размер OrderedDict более чем в два раза превышает размер обыч-
# ного словаря из-за содержащегося внутри дополнительного списка. А если вы со-
# бираетесь создать структуру данных, в которой будет большое число экземпляров
# OrderedDict (например, вы хотите прочитать 100 000 строк CSV-файла в список
# экземпляров OrderedDict), вам стоит изучить требования вашего приложения,
# чтобы решить, перевесят ли преимущества использования OrderedDict затраты на
# дополнительную память.
"""

########################################
# СТРОКИ И ТЕКСТ
########################################
"""
# 2.1 Разрезание строк различными разделителями
###############################################
# Вам нужно разделить строку на поля, но разделители (и пробелы вокруг них)
# внутри строки разные.
line = 'asdf fjdk; afed, fjek,adfs,      foo'
import re
text = re.split(r'[;,\s]\s*', line)
print(text)
# При применении re.split() вы должны быть осторожными, если шаблон регуляр-
# ного выражения использует группу, заключенную в скобки. При использовании
# групп совпавший с шаблоном текст также включается в результат.
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
# Получение символов-разделителей может быть полезным в некоторых обстоятельствах.
# Например, вам могут потребоваться эти символы позже – для перефор-
# матирования выводимой строки
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)
"""

########################################
# ИТЕРАТОРЫ И ГЕНЕРАТОРЫ
########################################

"""
# 4.1
# Ручное прохождение по итератору
#################################
# Вам нужно обработать элементы итерируемого объекта, но по какой-то причине
# вы не хотите использовать цикл.
with open('etc/passwd.txt') as f:
	try:
		while True:
			line = next(f)
			print(line, end='')
	except StopIteration:
		pass
# используя None
with open('etc/passwd.txt') as f:
	while True:
		line = next(f, None)
		if line is None:
			break
		print(line, end='')

# В большинстве случаев для прохода по итерируемому объекту используется цикл
# for. Однако задачи иногда требуют более точного контроля лежащего в основе
# механизма итераций. Также это полезно, для того чтобы разобраться, как он работает.
#####################################################################################
items = [1,2,3]
it = iter(items)	# Вызываем итератор
print(next(it))	# Вызываем it.__next__()
print(next(it))
print(next(it))
print(next(it))
"""

"""
# 4.2
# Делегирование итерации
########################
# Вы создали нестандартный объект-контейнер, который внутри содержит список,
# кортеж или какой-то другой итерируемый объект. Вы хотите заставить ваш новый
# контейнер работать с итерациями.

class Node:
	def __init__(self, value):
		self._value = value
		self._children = []

	def __repr__(self):
		return 'Node({!r})'.format(self._value)

	def add_child(self, node):
		self._children.append(node)

	def __iter__(self):
		return iter(self._children)

if __name__ == '__main__':
	root = Node(0)
	child1 = Node(1)
	child2 = Node(2)
	root.add_child(child1)
	root.add_child(child2)
	for ch in root:
		print(ch)
"""

"""
#4.3
# Создание новых итерационных паттернов с помощью генераторов
#############################################################
# Вы хотите реализовать собственный паттерн итераций, который будет отличаться
# от обычных встроенных функций (таких как range(), reversed() и т. п.).

def frange(start, stop, increment):
	x = start
	while x < stop:
		yield x
		x += increment

for n in frange(0, 4, 0.5):
	print(n)

print(list(frange(0, 1, 0.125)))

# Обсуждение
############
# Само присутствие инструкции yield в функции превращает ее в генератор. В отли-
# чие от обычной функции, генератор запускается только в ответ на итерацию. Вот
# эксперимент, который вы можете провести, чтобы понять внутренний механизм
# работы таких функций:

def countdown(n):
	print('Starting to count from', n)
	while n > 0:
		yield n
		n -= 1
	print('Done!')

c = countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))

# Ключевая особенность функции-генератора состоит в том, что она запускается
# только в ответ на операции next в ходе итерирования. Когда генератор возвра-
# щает значение, итерирование останавливается. Однако цикл for, который обычно
# используется для выполнения итераций, сам заботится об этих деталях, поэтому
# в большинстве случаев вам не стоит волноваться о них.
"""


"""
#4.5
# Вы хотите проитерировать по последовательности в обратном порядке.
####################################################################

a = [1, 2, 3, 4]
for x in reversed(a):
	print(x)

# Выводит файл задом наперед
#############################
f = open('somefile.txt')
for line in reversed(list(f)):
	print(line, end='')	

# Обсуждение
############
# Многие программисты не знают, что итерирование в обратном порядке может
# быть переопределено в собственном классе, если он реализует метод __reversed__().

class Countdown:
	def __init__(self, start):
		self.start = start

	# Прямой итератор
	def __iter__(self):
		n = self.start
		while n>0:
			yield n
			n -= 1

	# Обратный итератор
	def __reversed__(self):
		n = 1
		while n <= self.start:
			yield n
			n += 1
# Определение обратного итератора делает код намного более эффективным,
# а также снимает необходимость предварительного помещения данных в список
# для выполнения итераций в обратном порядке.
"""

########################################
# КОДИРОВАНИЕ И ОБРАБОТКА ДАННЫХ
########################################

"""
# 6.1 Чтение и запись данных в формате CSV
##########################################
# Вы хотите прочесть или записать данные в CSV-файл
######################################################
import csv
with open('stocks.csv') as f:
	f_csv = csv.reader(f)
	headers = next(f_csv)
	for row in f_csv:
		print(row)
"""
"""
# Поскольку такое индексирование часто может быть запутанным, вы можете за-
# хотеть использовать именованные кортежи.
import csv
from collections import namedtuple
with open('stocks.csv') as f:
	f_csv = csv.reader(f)
	headings = next(f_csv)
	Row = namedtuple('Row', headings)
	for r in f_csv:
		row = Row(*r)
		print(row)
"""

"""
# Еще одна альтернатива – прочесть данные в виде последовательности слова-
# рей.
import csv
with open('stocks.csv') as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		print(row)
"""

"""
# Чтобы записать данные в CSV, вы также можете использовать модуль csv, но
# создавая объект writer.
import csv

headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
]

with open('stocks_write.csv', 'w') as f:
	f_csv = csv.writer(f)
	f_csv.writerow(headers)
	f_csv.writerows(rows)
"""

"""
import csv
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
{'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
{'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
]

with open('stocks_write_dict.csv', 'w') as f:
	f_csv = csv.DictWriter(f, headers)
	f_csv.writeheader()
	f_csv.writerows(rows)
"""

#######################
# ОБСУЖДЕНИЕ
#######################

# Продолжение на странице 186 - 187



########################################
# ФУНКЦИИ
########################################


"""
# 7.1
# Определение функций, принимающих любое количество аргументов
###############################################################

# Вы хотите определить функцию, которая принимает любое количество аргумен-
# тов.
def avg(first, *rest):
	return (first + sum(rest)) / (1 + len(rest))
print(avg(1, 2))
print(avg(1, 2, 3, 4))

# Чтобы принять любое количество именованных аргументов, используйте аргу-
# мент, который начинается с **.
import html

def make_element(name, value, **attrs):
	keyvals = [' %s="%s"' % item for item in attrs.items()]
	attr_str = ''.join(keyvals)
	element = '<{name}{attrs}>{value}</{name}>'.format(
				name=name,
				attrs=attr_str,
				value=html.escape(value))
	return element

file = open ('index.html', 'w')
file.write(make_element('item', 'Albatross', size='large', quantity=6))
file.write(make_element('p', '<spam>'))
file.close()

# Обсуждение
#############
# Аргумент со * может быть только последним в списке позиционных аргументов
# в определении функции. Аргумент с ** может быть только последним. Тонкость
# тут в том, что аргумент без звездочки может идти и после аргумента со звездоч-
# кой
def a(x, *args, y):
	pass
def b(x, *args, y, **kwargs):
	pass
"""

"""
###################
# КЛАССЫ И ОБЪЕКТЫ
###################
# 8.1
# Изменение строкового представления экземпляров
################################################
# Вы хотите изменить строки, которые выдаются при выводе или просмотре экземпляров,
# на что-то более понятное.
class Pair:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return 'Pair({0.x!r}, {0.y!r})'.format(self)
	def __str__(self):
		return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3,4)
#>>>p # в IDLE вывод __repr__()
print(p) # __str__ метод
print('p is {0!r}'.format(p))
# Определение __repr__() и __str__() часто является хорошей практикой, поскольку
# может облегчить отладку и вывод экземпляра. Например, просто печатая или ло-
# гируя экземпляр, программист получит более полезную информацию о содержи-
# мом экземпляра.
"""

"""
# 8.16
#??? Определение более одного конструктора в классе
################################################
# Вы пишете класс и хотите, чтобы пользователи могли создавать экземпляры не
# только лишь единственным способом, предоставленным __init__().
import time

class Date:
	# Основной конструктор
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

	# Альтернативный конструктор
	@classmethod
	def today(cls):
		t = time.localtime()
		return cls(t.tm_year, t.tm_mon, t.tm_mday)

a = Date(2012, 12, 21)	# Первичный
b = Date.today() # Альтернативный
"""

################################################
# ПОЛЕЗНЫЕ СКРИПТЫ И СИСТЕМНОЕ АДМИНИСТРИРОВАНИЕ
################################################

"""
# 13.15
# Запуск браузера
#################
# Вы хотите запустить браузер из скрипта и заставить его открыть указанный вами
# URL.
import webbrowser
webbrowser.open('http://www.python.org')
# Открыть страницу в новом окне браузера
webbrowser.open_new('http://www.python.org')
# Открыть страницу в новой вкладке браузера
webbrowser.open_new_tab('http://www.python.org')

# ОБСУЖДЕНИЕ
#############
# Возможность легко запустить браузер может оказаться весьма кстати в некото-
# рых скриптах. Например, скрипт может выполнять некий деплоймент на сервер,
# и вы хотите заставить его также быстро запустить браузер, чтобы удостовериться,
# что все работает. Или же программа может записывать данные в форме HTML-
# страниц, и вы просто хотите сразу посмотреть результат. В обоих случаях модуль
# webbrowser будет простым решением.
"""