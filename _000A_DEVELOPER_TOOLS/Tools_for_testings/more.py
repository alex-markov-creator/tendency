"""
more.py - Разбивает строку или текстовый файл на страницы для интерактивного просмотра
"""
def more(text, numlines=30):
    lines = text.splitlines() # подобно split('\n') но без '' в конце
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('Enter-->') not in ['']: break

if __name__ == '__main__':
    import sys # если запускается как сценарий
    more(open(sys.argv[1], encoding='utf-8').read(), 30) # отобразить постранично содержимое файла, указанного в командной строке