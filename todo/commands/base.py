# -*- coding: utf-8 -*-

from __future__ import absolute_import

import sys
import json

from todo.utils.styles import Fore, Style


class Command:
    def __init__(self):
        self.usage = None
        self.description = None
        self.PROJECT_FILE = 'tasks.json'
        self.UNTITLED_NAME = 'Untitled'

    def get_project_name(self):
        try:
            with open(self.PROJECT_FILE, 'r') as project_file:
                data = json.load(project_file)
                name = data['name']
        except:
            return self.UNTITLED_NAME

        return name if name else self.UNTITLED_NAME

    def get_command_name(self):
        try:
            return '{} {}'.format(sys.argv[0].split('/')[-1], sys.argv[1])
        except:
            return sys.argv[0]

    def get_command_attributes(self):
        try:
            return ' '.join(sys.argv[2:])
        except:
            return None

    def get_titles_input(self):
        titles_input = self.get_command_attributes()

        if not titles_input:
            print(
                '{info}Empty item ignored{reset}'
                    .format(
                    info=Fore.INFO,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit()

        titles = titles_input.split(',')
        return [title.strip() for title in titles if title is not '']

    def cancel_command(self):
        print(
            '\n{fail}{command}{reset} canceled'
                .format(
                command=self.get_command_name(),
                fail=Fore.FAIL,
                reset=Style.RESET_ALL
            )
        )
        sys.exit()

    def project_not_found(self):
        print(
            '{fail}No project found{reset}'
                .format(
                fail=Fore.FAIL,
                reset=Style.RESET_ALL,
            )
        )
        sys.exit(1)

    def ask_create_project(self):
        try:
            answer = input(
                '{warning}No project found, create one first?{reset} (y/n) '
                    .format(
                    warning=Fore.WARNING,
                    reset=Style.RESET_ALL,
                )
            ).lower()
        except KeyboardInterrupt:
            self.cancel_command()

        if answer.startswith('n'):
            sys.exit()

        from todo.commands.project import Init
        Init.run()

    def update_project(self, new_data):
        try:
            with open(self.PROJECT_FILE, 'w', encoding='utf-8') as project_file:
                json.dump(
                    new_data,
                    project_file,
                    sort_keys=True,
                    indent=4,
                    ensure_ascii=False,
                )
        except:
            print(
                '{fail}An error has occured while updating the project.{reset}'
                    .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit(1)
