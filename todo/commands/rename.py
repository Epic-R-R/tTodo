from __future__ import absolute_import

import sys
import json

from todo.commands.base import Command
from todo.utils.styles import Fore, Style


class RenameCommand(Command):
    def rename_project(self, data):
        data_copy = data.copy()
        new_name = self.get_command_attributes()

        if new_name:
            data_copy['name'] = self.get_command_attributes()
            return data_copy
        else:
            print(
                '{info}No name specified.{reset}'
                .format(
                    info=Fore.INFO,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit()


    def run(self):
        try:
            with open(self.PROJECT_FILE, 'r') as project_file:
                data = json.load(project_file)
        except FileNotFoundError:
            self.project_not_found()
        except:
            print(
                '{fail}An error has occured while renaming the todos.{reset}'
                .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit(1)

        self.update_project(self.rename_project(data))


Rename = RenameCommand()