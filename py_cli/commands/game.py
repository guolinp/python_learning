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
def run(ctx):
    ctx.obj.container.game.run()


if __name__ == '__main__':
    cli(obj={})
