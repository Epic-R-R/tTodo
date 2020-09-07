from __future__ import absolute_import

from todo.commands.project import Init
from todo.commands.list import List
from todo.commands.add import Add
from todo.commands.remove import Remove
from todo.commands.toggle import Toggle
from todo.commands.check import Check
from todo.commands.uncheck import Uncheck
from todo.commands.search import Search
from todo.commands.delete import Delete
from todo.commands.rename import Rename

commands_dict = {
    'project': Init.run,
    'list': List.run,
    'ls': List.run,
    'add': Add.run,
    'remove': Remove.run,
    'rm': Remove.run,
    'toggle': Toggle.run,
    'tg': Toggle.run,
    'check': Check.run,
    'uncheck': Uncheck.run,
    'search': Search.run,
    'delete': Delete.run,
    'del': Delete.run,
    'rename': Rename.run,
}
