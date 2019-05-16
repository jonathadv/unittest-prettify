import inspect

from .colors import RESET


def prettify(color=RESET, template=None):
    def wrap(something):
        if inspect.isclass(something):
            _handle_class(something, color, template)
        else:
            _handle_function(something, color, template)

        return something

    return wrap


def _handle_class(_class, color, template):
    for _, member in _class.__dict__.items():
        _handle_function(member, color, template)


def _handle_function(_member, color, template):
    if inspect.ismethod(_member) or inspect.isfunction(_member):
        if _member.__doc__:
            if not _member.__doc__.startswith(
                "\u001b["
            ) and not _member.__doc__.endswith(RESET):
                _member.__doc__ = _design_line(_member.__doc__, color, template)


def _design_line(content, color, template):
    if not template:
        template = "{color}{content}{reset}"
    value = (
        template.replace("{color}", color)
        .replace("{content}", content)
        .replace("{reset}", RESET)
    )
    return value
