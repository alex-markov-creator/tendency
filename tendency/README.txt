Microsoft Windows [Version 10.0.19041.572]
Версия - 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)]

Установка интерпретатора:
python-3.8.5.exe (при установке обязательно поставить флажок add PATCH)

Файл зависимостей - requirements.txt

Установка виртуальной среды и зависимости:
py -m venv <Наименование>
pip install -r requirements.txt

Зависимости:
certifi==2020.6.20
cycler==0.10.0
kiwisolver==1.2.0
matplotlib==3.3.1
numpy==1.19.1
pandas==1.1.1
Pillow==7.2.0
pyparsing==2.4.7
python-dateutil==2.8.1
pytz==2020.1
scipy==1.5.2
seaborn==0.10.1
six==1.15.0
XlsxWriter==1.3.6
xlrd==1.2.0
tabulate==0.8.7
prettytable==1.0.1

Под виндой из CMD запускать:
- adhaesio.bat (или просто adhaesio)::путь файла adhaesio.py;
- control_production.bat (или просто control_production)::путь файла control_production.py(w);
- production.bat (или просто production)::путь файла production;
- project_develop.bat (или просто production)::путь файла project_develop.py;
- consumer.bat (или просто consumer)::путь файла consumer.py;
- people.bat (или просто people)::путь файла people.py;
- results.bat (или просто results)::путь файла linear.py(w).
В случае необходимости составления файлов формата .bat:
- help_command_bat.txt.
