import click
from ..cookie.most_active import most_active_cookie


@click.group()
def cookie():
    pass


@click.command("most_active")
@click.option('-f', '--file_name', required=True, type=str)
@click.option('-d', '--day', required=True, type=click.DateTime(formats=["%Y-%m-%d"]))
def most_active(file_name, day):
    most_active_cookie(file_name,day)


cookie.add_command(most_active)

