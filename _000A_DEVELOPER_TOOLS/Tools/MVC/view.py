# -*- coding:utf-8 -*-
"""
"""
from models import Storage #
from commands import (
    Intro,
    InfoCommand,
    ScoreCommand,
    AddCommand,
    DelCommand,
    NoteCommand,
    ExitCommand,
    UserExitException,
    NewCommand,  # до последующих версий, реализация исключения NotImplemented()
    )

def get_routes():
    """
    Функция наименований выполняемых комманд реализованная используя словари.
    :return: `dict` of possible commands, with the format: `name -> class`
    """
    return {
        '1': InfoCommand,
        '2': ScoreCommand,
        '3': AddCommand,
        '4': DelCommand,
        'exit': ExitCommand,
        '5': NoteCommand,
        '6': NewCommand,
    }

def perform_command(command):
    """
    Выполнение команды по наименованию.
    Сохраняет результат в 'Storage()'.
    :param command: command name, selected by user.
    """
    command = command.lower()
    routes = get_routes()

    try:
        command_class = routes[command]
        command_inst = command_class()
        storage = Storage()
        command_inst.perform(storage.items)
    except KeyError:
        print('Неправильная команда, попробуйте снова!!!')
    except UserExitException as ex:
        print(ex)
        raise

def main():
    """
    Основной метод работает бесконечно, пока пользователь не запустит команду 'exit'.
    Или нажмёт 'Ctrl + C' в консоли.
    """
    while True:
        try:
            command = parse_user_input()
            perform_command(command)
        except UserExitException:
            break
        except Exception as e:
            print('Здесь пока ничего.')

def parse_user_input():
    """
    Пользовательский ввод input()
    :return: `str` с введенными данными.
    """
    # Наименование комманд из списка ключей словаря комманд
    input_function = input
    message = '\nВыберите пункт: (%s): ' % '|'.join(
        {
            InfoCommand.label(): InfoCommand,
            ScoreCommand.label(): ScoreCommand,
            AddCommand.label(): AddCommand,
            DelCommand.label(): DelCommand,
            NoteCommand.label(): NoteCommand,
            ExitCommand.label(): ExitCommand
        }.keys()
    )
    return input_function(message)

