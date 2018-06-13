#!/usr/bin/python -tt

from game import Game
from music import Music


class Container:

    """ This is the class that exports the App python bindings."""

    # This defines each of our apps and the constructor method.
    apps = [{"name": "game", "constructor": Game},
            {"name": "music", "constructor": Music}
            ]

    def __init__(self, name):
        self.name = name
        for info in Container.apps:
            setattr(self, info['name'], info['constructor'](self.name))

    def destroy(self):
        for info in Container.apps:
            app = getattr(self, info['name'])
            app.__exit__(0, 0, 0)
            setattr(self, info['name'], None)
