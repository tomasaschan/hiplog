import click

from hiplog.model.projections import all_items


def register(parent):
    @parent.command("list-items")
    def list_items_cli():
        for id, item in all_items().items():
            click.echo(f"\n{item.type.name}: {id}")
            click.echo(f"Created {item.created_at}, {item.notes[0].title}")
            if len(item.parents) > 0:
                click.echo(f"Parents: {','.join(p.id for p in item.parents)}")
            if len(item.children) > 0:
                click.echo(f"Children: {','.join(c.id for c in item.children)}")
