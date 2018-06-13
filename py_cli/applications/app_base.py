#!/usr/bin/python -tt


class AppBase(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        return self

    def __exit__(self, exc_type=None, exc_value=None, traceback=None):
        return

    def run(self):
        pass
