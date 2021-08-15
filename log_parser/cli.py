import click
from .commands.cookie_parser import cookie


@click.group()
def cli():
    pass


cli.add_command(cookie)
