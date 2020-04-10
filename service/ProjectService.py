import os
from datetime import datetime


def format_date(date: datetime):
    return date.strftime('%Y-%m-%d')


user_data_directory = '~/.TimeTracker/'
root_directory = os.path.expanduser(user_data_directory)
data_directory = root_directory + 'user-data'
configuration_location = root_directory + 'data'


class ProjectService:
    def __init__(self):
        self.current_version = None
        self.project_name = None
        self.__load()

    def __load(self):
        with open(configuration_location, 'r') as f:
            lines = f.readlines()
            self.project_name = lines[0].strip()
            if len(lines) > 1 and len(lines[1]) > 1:
                self.current_version = lines[1].strip()
            print(self.project_name, self.current_version)

    def get_current_filename(self):
        return data_directory + '/' + self.project_name + '/' + self.get_version()

    def change_project(self, new_project: str):
        self.project_name = new_project
        try:
            os.mkdir(data_directory + '/' + new_project)
            print('A new directory has been created.')
        except:
            print('Directory already created.')
        self.__write_configuration()

    def __write_configuration(self):
        with open(configuration_location, 'w') as f:
            f.write(self.project_name + '\n')
            if self.current_version is not None:
                f.write(self.current_version + '\n')

    def get_version(self):
        if self.current_version is None:
            print(format_date(datetime.today()))
            return format_date(datetime.today())
        else:
            return self.current_version

    def change_current_version(self, year, month, day):
        self.current_version = format_date(datetime(year, month, day))
        self.__write_configuration()

    def remove_version(self):
        self.current_version = None
        self.__write_configuration()
