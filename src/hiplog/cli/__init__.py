import click

from hiplog.cli.createitem import register as register_create_item
from hiplog.cli.debug import register as register_debug


@click.group()
def cli():
    pass


register_create_item(cli)
register_debug(cli)
