from __future__ import absolute_import

import os
import sys
import json

from todo.commands.toggle import ToggleCommand


class UncheckCommand(ToggleCommand):
    def check_by_item(self, item):
        item_toggled = item.copy()
        item_toggled['done'] = False
        return item_toggled


Uncheck = UncheckCommand()
