import click
from .commands.cookie_parser import cookie


@click.group()
def cli():
    """
    Click Group for handling all supporting commands
    :return: None
    """
    pass


cli.add_command(cookie)
