from __future__ import absolute_import
from todo.commands.toggle import ToggleCommand


class RemoveCommand(ToggleCommand):
    def get_subtitle(self):
        return 'Remove items'

    def click(self, todos, item_index):
        todos_removed = todos.copy()
        todos_removed.pop(item_index)
        return todos_removed

    def search(self, todos, item):
        todos_removed = todos.copy()
        todos_removed.remove(item)
        return todos_removed


Remove = RemoveCommand()
