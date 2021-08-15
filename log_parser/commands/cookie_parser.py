import click
from ..cookie.most_active import most_active_cookie


@click.group()
def cookie():
    """
    This is the group that has all commands supported for cookie
    :return: None
    """
    pass


@click.command("most_active")
@click.option('-f', '--file_name', required=True, type=str, help='file name')
@click.option('-d', '--day', required=True, type=click.DateTime(formats=["%Y-%m-%d"]), help='date in "%Y-%m-%d" format')
def most_active(file_name, day):
    """
    This Command calls function for most active cookie for the given date
    :param file_name: file name
    :param day: requested date
    :return: None
    """
    try:
        solution = most_active_cookie(file_name, day)
        for cookie in solution:
            click.echo(cookie)
    except Exception as e:
        click.echo(e)


cookie.add_command(most_active)

