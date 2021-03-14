from re import MULTILINE, finditer


class Note:
    def __init__(self, path: str):
        self.path = path
        with open(self.path, "r") as f:
            self.content = f.read()

    @property
    def title(self):
        all_h1_mathes = finditer(r"^#\s+(.+)$", self.content, MULTILINE)
        all_match_groups = (
            group for match in all_h1_mathes for group in match.groups()
        )
        first_h1 = next(all_match_groups)
        return first_h1
