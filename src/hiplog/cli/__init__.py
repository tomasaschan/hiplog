import click

from hiplog.cli.createitem import register as register_create_item


@click.group()
def cli():
    pass


register_create_item(cli)
