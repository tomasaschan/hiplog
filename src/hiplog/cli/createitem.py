import datetime

import click

from hiplog.cli.helpers import datetime_with_zoneinfo, parse_enum
from hiplog.model import createitem


def register(parent):
    @parent.command()
    @click.option(
        "--timestamp",
        type=click.DateTime(),
        required=True,
        callback=datetime_with_zoneinfo,
    )
    @click.option(
        "--type",
        type=click.Choice(createitem.ItemType.__members__),
        required=True,
        callback=parse_enum(createitem.ItemType),
    )
    @click.option("--id", type=str, required=True)
    @click.option("--note", type=click.File(), required=True)
    def create_item(
        timestamp: datetime.datetime,
        type: createitem.ItemType,
        id: str,
        note: click.File,
    ):
        createitem.create_item(timestamp, type, id, note)
