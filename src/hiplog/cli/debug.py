import click


from hiplog import db


def register(parent):
    @parent.group()
    def debug():
        """A place to hide dummy stuff"""
        pass

    @debug.command()
    def list_events():
        """Read and parse the events file, and list all events"""

        for event in db.read_events():
            click.echo(event)
