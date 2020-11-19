ЗАДАЧА А: Используя принципы ООП (Объектно-ориентированного программирования):
	- Наследование;
	- Инкапсуляция;
	- Полиморфизм.

1 Подзагрузка файлов формата .csv в файл __init__ расположенный в каталоге DATA_CSV - инкапсуляция переменных;
2 Определить визуальный ряд необходимых графиков:
- Линейный график средствами библиотеки matplotlib;
- Диаграмма плотности ("ящик с усами") средствами seaborn;
- Гистограмма распределения средствами seaborn;
- Точечные графики характеризующую кореляционную зависимость - cobfidence_ellipse.py:
	+ https://matplotlib.org/gallery/statistics/confidence_ellipse.html#sphx-glr-gallery-statistics-confidence-ellipse-py
3 Определить допустимую погрешность при измерении показателей характеризующих адгезию:
- Построить график погрешностей типа errorbar средствами matplotlib - Errorbar_graphics.py:
	+ https://ru.stackoverflow.com/questions/720404/%D0%9A%D0%B0%D0%BA-%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA%D0%B8-%D1%81-%D0%BF%D0%BE%D0%B3%D1%80%D0%B5%D1%88%D0%BD%D0%BE%D1%81%D1%82%D1%8F%D0%BC%D0%B8-%D0%B2-python
4 Вывод возможных графиков в компановке с помощью subplots - оффициальная документация matplotlib;
	+https://matplotlib.org/tutorials/intermediate/tight_layout_guide.html#sphx-glr-tutorials-intermediate-tight-layout-guide-py 
5 Построение графиков организовать в отдельном модуле graphics.py:

.-
  - DATA_CSV
    __init__.py
    -...csv;
    - ...
  - adhaesio.py
  - graphics
    - __init__.py
    - graphics.py

,где . - корневой каталог.

ЗАДАЧА Б: