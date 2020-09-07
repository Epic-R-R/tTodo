class TodoError(Exception):
    """todo exception"""


class CommandError(TodoError):
    """Just raised when there is an error in command-line arguments"""