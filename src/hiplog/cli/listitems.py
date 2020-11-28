from hiplog.model.projections import all_items


def register(parent):
    @parent.command("list-items")
    def list_items_cli():
        for id, item in all_items().items():
            print(f"\n{id}")
            print(f"Created {item.created_at}")
            if len(item.parents) > 0:
                print(f"Parents: {','.join(p.id for p in item.parents)}")
            if len(item.children) > 0:
                print(f"Children: {','.join(c.id for c in item.children)}")
