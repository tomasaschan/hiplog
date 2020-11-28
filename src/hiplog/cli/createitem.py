import datetime

import click

from hiplog.cli.helpers import datetime_with_zoneinfo, parse_enum
from hiplog.model.createitem import ItemIdExists, create_item
from hiplog.model.events import ItemType


def register(parent):
    @parent.command("create-item")
    @click.option(
        "--timestamp",
        type=click.DateTime(),
        required=True,
        callback=datetime_with_zoneinfo,
    )
    @click.option(
        "--type",
        type=click.Choice(ItemType.__members__),
        required=True,
        callback=parse_enum(ItemType),
    )
    @click.option("--id", type=str, required=True)
    @click.option("--note", type=click.File(), required=True)
    def create_item_cli(
        timestamp: datetime.datetime,
        type: ItemType,
        id: str,
        note: click.File,
    ):
        try:
            create_item(timestamp, type, id, note)
        except ItemIdExists as ex:
            raise click.ClickException(str(ex))
