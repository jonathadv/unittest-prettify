import inspect


RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
BLUE = "\u001b[34m"
MAGENTA = "\u001b[35m"
WHITE = "\u001b[37m"
RESET = "\u001b[0m"


def colorize(color=WHITE):
    def wrap(something):
        if inspect.isclass(something):
            _handle_class(something, color)
        else:
            _handle_function(something, color)

        return something

    return wrap


def _handle_class(_class, color):
    for _, member in _class.__dict__.items():
        _handle_function(member, color)


def _handle_function(_member, color):
    if inspect.ismethod(_member) or inspect.isfunction(_member):
        if _member.__doc__:
            if not _member.__doc__.startswith(
                "\u001b["
            ) and not _member.__doc__.endswith(RESET):
                _member.__doc__ = f"{color}{_member.__doc__.strip()}{RESET}"
