import click


@click.group()
def cli():
    pass


@cli.command()
def hello():
    """Say hello"""
    click.echo("hello")
