#!/usr/bin/python -tt

import click


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    if ctx.obj.debug:
        click.echo("starting debug")


@cli.command()
@click.pass_context
#@click.option('--name', "-n", default=None, help='music name')
@click.argument('name')
def start(ctx, name):
    if name is None:
        click.echo('music name missing')
    else:
        ctx.obj.container.music.start(name)


@cli.command()
@click.pass_context
@click.option('--name', "-n", default=None, help='music name')
def stop(ctx, name):
    ctx.obj.container.music.stop(name)


if __name__ == '__main__':
    cli(obj={})
