#!/usr/bin/python


class Color(object):
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"


def set_color(string, color):
    return color + string + Color.RESET

string = set_color("This should be a red line.", Color.RED)

print(string)
