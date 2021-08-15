import click


@click.command()
@click.option('-f', '--file_name', required=True, type=str)
@click.option('-d', '--day', required=True, type=click.DateTime(formats=["%Y-%m-%d"]))
def cookie(file_name, day):
    click.echo(f"file={file_name} day={day.date()}")
