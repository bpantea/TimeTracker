#!/usr/bin/python3
import os
import sys

source_code_directory = '~/PycharmProjects/TimeTracker'

sys.path.append(os.path.expanduser(source_code_directory))

from repository.TimeEventRepository import TimeEventRepository
from service.ProjectService import ProjectService
from service.timeservice import TimeService

project_service = ProjectService()
repo = TimeEventRepository(project_service.get_current_filename())
print('Active project filename:', repo.filename)
time_service = TimeService(repo)


class Operation:
    def __init__(self, function, docs, arguments):
        self.arguments = arguments
        self.docs = docs
        self.function = function

    def check_arguments(self, args):
        if isinstance(self.arguments, int) and len(args) != self.arguments:
            self.__exit_with_docs()
        elif isinstance(self.arguments, list) and len(args) not in self.arguments:
            self.__exit_with_docs()

    def __exit_with_docs(self):
        print('Are you sure you are using this right?')
        print(self.docs)
        exit(1)

    def exec(self, args):
        self.check_arguments(args)
        self.function(args)


def start_time(args):
    if len(args) == 2:
        time_service.start_time(int(args[0]), int(args[1]))
    else:
        time_service.start_time()
    print(time_service.formatted_time())


def end_time(args):
    if len(args) == 2:
        time_service.end_time(int(args[0]), int(args[1]))
    else:
        time_service.end_time()
    print(time_service.formatted_time())


def set_time(args):
    time_service.set_time(int(args[0]), int(args[1]))
    print(time_service.formatted_time())


def check_time(args):
    print(time_service.formatted_time())


def change_project(args):
    project_service.change_project(str(args[0]))
    print('Project changed.')


def custom_date(args):
    project_service.change_current_version(int(args[0]), int(args[1]), int(args[2]))
    print('Date was changed to: ', project_service.get_version())


def remove_custom_date(args):
    project_service.remove_version()
    print('Date was changed to today (' + project_service.get_version() + ')')


def show_doc(args):
    for command in runner:
        print(command, '---', runner[command].docs)


runner = {
    'start': Operation(start_time,
                       'Can be used without arguments, then the current time will be taken or 2 arguments: hours and '
                       'minutes',
                       [0, 2]),
    'end': Operation(end_time,
                     'Can be used without arguments, then the current time will be taken or 2 arguments: hours and '
                     'minutes',
                     [0, 2]),
    'set': Operation(set_time, '2 arguments necessary: hours and minutes', 2),
    'check': Operation(check_time, 'No arguments are necessary', 0),
    'change': Operation(change_project, 'One argument containing the new name of the project', 1),
    'date': Operation(custom_date, '3 integers: year, month, day', 3),
    'today': Operation(remove_custom_date, 'No arguments are necessary', 0),
    'help': Operation(show_doc, 'This shit', 0)
}


def run():
    arguments = sys.argv
    if len(arguments) < 2:
        show_doc(None)
        exit(1)
    command = arguments[1]
    arguments = arguments[2:]
    if command in runner:
        runner[command].exec(arguments)
    else:
        print('Command not found.')
        print('List of commands: ', runner.keys())


run()
