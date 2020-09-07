from __future__ import absolute_import

import sys
import json

from todo.commands.base import Command
from todo.utils.menu import show_options
from todo.utils.styles import Fore, Style


class ToggleCommand(Command):
    def get_subtitle(self):
        return 'Items'

    def check_by_item(self, item):
        item_toggled = item.copy()
        status = item['done']
        item_toggled['done'] = not status
        return item_toggled

    def click(self, todos, item_index):
        todos_toggled = todos.copy()
        item_to_toggle = todos[item_index]
        todos_toggled[item_index] = self.check_by_item(item_to_toggle)
        return todos_toggled

    def search(self, todos, item):
        todos_toggled = todos.copy()
        item_index = todos_toggled.index(item)
        item_to_toggle = todos_toggled[item_index]
        todos_toggled[item_index] = self.check_by_item(item_to_toggle)
        return todos_toggled

    def open_list(self, data, name):
        if len(data['todos']) == 0:
            raise KeyError
        try:
            return show_options(
                name,
                self.get_subtitle(),
                data['todos'],
                self.click
            )
        except KeyboardInterrupt:
            self.cancel_command()

    def update_todos(self, data):
        new_data = data.copy()
        items_titles = self.get_titles_input()
        options_all = ['-a', '--all']
        todos = new_data['todos']

        if items_titles[0].lower() in options_all:
            for item in todos:
                todos = self.search(todos, item)
        else:
            items_matching = [item for item in todos if item['title'] in items_titles]
            if items_matching:
                for item_found in items_matching:
                    todos = self.search(todos, item_found)

            titles_matching = [item['title'] for item in items_matching]
            items_not_found = [item for item in items_titles if item not in titles_matching]
            if items_not_found:
                print(
                    '{info}Unknown {items_print}: {items}{reset}'
                        .format(
                        info=Fore.INFO,
                        reset=Style.RESET_ALL,
                        items_print=('items' if len(items_not_found) > 1 else 'item'),
                        items=', '.join(items_not_found),
                    )
                )

            if not items_matching:
                sys.exit()

        return todos

    def run(self):
        try:
            with open(self.PROJECT_FILE, 'r') as project_file:
                data = json.load(project_file)
        except FileNotFoundError:
            self.project_not_found()
        except KeyError:
            print(
                '{fail}An error has occured while toggling the todos.{reset}'
                    .format(
                    fail=Fore.FAIL,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit(1)

        try:
            name = data['name']
        except:
            name = self.UNTITLED_NAME

        try:
            if self.get_command_attributes():
                new_todos = self.update_todos(data)
            else:
                new_todos = self.open_list(data, name)
        except KeyError:
            print(
                '{warning}No items in the project.{reset}'
                    .format(
                    warning=Fore.WARNING,
                    reset=Style.RESET_ALL,
                )
            )
            sys.exit()

        new_data = {
            'name': name,
            'todos': new_todos
        }

        self.update_project(new_data)


Toggle = ToggleCommand()
