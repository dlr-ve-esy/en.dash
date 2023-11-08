from attr import field, define
import cattr
import pathlib as pt
import json
import collections

TabData = collections.namedtuple("TabData", ["id", "label"])


# cattr hooks
cattr.register_structure_hook(TabData, lambda i, t: t(**i))
cattr.register_unstructure_hook(TabData, lambda i: i._asdict())


@define
class DashboardConfiguration:
    enable_darkmode_toggle: bool = field(default=True)
    enable_references: bool = field(default=True)
    tabs: list[TabData] = field(factory=lambda: [TabData("references", "References")])
    references: list[str] = field(factory=list)
    dashboard_label: str = field(default="title of dashboard")

    @classmethod
    def load(cls, path: pt.Path):
        if path.exists():
            with path.open("r") as ipf:
                data = json.load(ipf)
            return cattr.structure(data, cls)
        else:
            return cls()

    def save(self, path):
        data = cattr.unstructure(self)
        with path.open("w") as opf:
            json.dump(data, opf)
