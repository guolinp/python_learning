#!/usr/bin/python -tt

import os
import click

from applications.container import Container


class Context(object):

    def __init__(self):
        self.debug = False

    def log(self, msg, *args):
        """log to stdout"""
        if args:
            msg %= args
        click.echo(msg, file=sys.stdout)

    def vblog(self, msg, *args):
        """Log to stdout if debug is on."""
        if self.debug:
            self.log(msg, *args)

    def init_container(self, name):
        self.container = Container(name)

    def __del__(self):
        self.container.destroy()


pass_context = click.make_pass_decorator(Context, ensure=True)
plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')


class Command(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']


@click.command(cls=Command)
@click.option('-d', '--debug', is_flag=True, help='Enables debug mode.')
@click.option('-n', '--name', default="default_container", help='The container name')
@pass_context
def cli(ctx, debug, name):
    """Container command line interface."""
    ctx.debug = debug
    ctx.init_container(name)


import argparse
import contextlib
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Application CLI", add_help=True)
    args, _ = parser.parse_known_args()

    cli(obj={})
