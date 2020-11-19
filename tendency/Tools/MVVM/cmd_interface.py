# -*- coding: utf-8 -*-
"""
cmd_commands.py -  реализация интерфейса коммандной строки
с помощью механизма интроспекции Python.
Структура - смотри паттерн MVVM.
Смотри по коду комментарий #NEW Commands для добавления новых комманд
"""
from abc import ABC, abstractmethod

class New_object(object):  # new_object = New_object()
    """
    Обычно метакласс переопределяет метод __new__ или __init__ класса type, с целью взять на себя управление созданием или инициализацией нового объекта класса. Как и при использовании декораторов классов, суть состоит в том, чтобы определить программный код, который будет вызываться автоматически на этапе создания класса. Оба способа позволяют расширять классы или возвращать произвольные объекты для его замены – протокол с практически неограниченными возможностями.
    """
    obj = None
    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj

class BaseCommand(ABC):
    """
    Абстрактным базовым классом (Abstract Base Class, ABC) называется
    класс, который не может использоваться для создания объектов.
    Назначение таких классов состоит в определении интерфейсов, то есть
    в том, чтобы перечислить методы и свойства, которые должны быть
    реализованы в классах, наследующих абстрактный базовый класс. Это
    удобно, так как можно использовать абстрактный базовый класс как
    своего рода договоренность - договоренность о том, что любые
    порожденные классы обеспечат реализацию методов и свойств, объявленных
    в абстрактном базовом.
    """
    @abstractmethod
    def label()->str:
        """
        Наименование комманды
        :return: str
        """
        pass

    def perform(self, object, *args, **kwargs):
        """
        Выполняемые инструкции
        """
        pass

class Interface_cmd(object):
    """
    Класс запуска интерфейса коммандной строки
    Пример:
    run = Interface()
    run.main()
    """
    def user_input(self):
        """
        Пользовательский ввод input()
        # Наименование комманд из класса 'dict_keys'
        :return: str
        """
        message = '{}: '.format('|'.join(
            {
                FirstCommand.label(): FirstCommand,
                SecondCommand.label(): SecondCommand,
                #NewCommand.label(): NewCommand,
                # NEW COMMANDs
                ExitCommand.label(): ExitCommand,
            }.keys()
        ))
        return input(message)

    def lst_commands(self):
        """
        Функция определения комманд
        :return: словарь со значением {input_function(message) : class}
        """
        return {
                '1': FirstCommand,
                '2': SecondCommand,
                '0': NewCommand,
                # NEW COMMANDs
                'exit': ExitCommand

        }

    def perform_command(self, command):
        """
        Выполнение команды по наименованию.
        Сохраняет результат в 'New_object()'.
        """
        try:
            command = command.lower()
            routes = self.lst_commands()
            command_class = routes[command]
            command_inst = command_class()
            new_object = New_object()
            command_inst.perform(new_object.items)
        except KeyError:
            print('Неправильная команда, попробуйте снова!!!')

    def main(self):
        """
        Функция запуска
        """
        while True:
            try:
                command = self.user_input()
                assert command != ''
                self.perform_command(command)
            except KeyboardInterrupt:
                print('Выход...')
                break
            except UserExitException:
                print('Выход...')
                break
            except AssertionError:
                pass
            except Exception:
                print('Здесь пока ничего')

class UserExitException(Exception): pass


###############################################################################
# NEW_COMMANDs
###############################################################################

class FirstCommand(BaseCommand):
    def label():
        return 'Комманда-1'

    def perform(self, object, *args, **kwargs):
        raise # NEW OBJECTs

class SecondCommand(BaseCommand):
    def label():
        return 'Комманда-2'

    def perform(self, object, *args, **kwargs):
        print("Новая комманда")

class NewCommand(BaseCommand):
    def label():
        return 'Комманда-0'

    def perform(self, object, *args, **kwargs):
        print("Новая комманда")
        return 'LoL'

class ExitCommand(BaseCommand):
    def label():
        return 'exit'

    def perform(self, object, *args, **kwargs):
        raise UserExitException

###############################################################################
# END NEW_COMMANDs
###############################################################################

if __name__=='__main__':
    run = Interface_cmd()
    run.main()