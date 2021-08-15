from os import path
import click
from .csv.count_day_sorted import count_day as csv_count


def most_active_cookie(file_name, day):
    if not path.exists(file_name):
        click.echo("File doesn't exists")
    cookie_count_by_day = {}
    if file_name.endswith('.csv'):
        cookie_count_by_day = csv_count(file_name, day)
    print(cookie_count_by_day)



