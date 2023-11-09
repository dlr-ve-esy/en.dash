from attr import field, define
import cattr
import pathlib as pt
import json
import collections

# cattr hooks
cattr.register_structure_hook(pt.Path, lambda i, t: t(i))
cattr.register_unstructure_hook(pt.Path, lambda i: i.as_posix())


@define
class TabData:
    id: str = field()
    label: str = field(default="tab")
    icon: str = field(default="bar-chart")
    text: str | None = field(default=None)
    path: pt.Path | None = field(default=None)
    display_infobox: bool = field(default=False)
    display_label: str = field(default="do you want to know more?")
    display_icon: str = field(default=":grey_question:")
    display_enabled: bool = field(default=True)

    tab_ref: None = field(default=None)


@define
class DashboardConfiguration:
    enable_darkmode_toggle: bool = field(default=True)
    enable_references: bool = field(default=True)
    tabs: list[TabData] = field(factory=lambda: [TabData("references", "References")])
    references: list[str] = field(factory=list)
    dashboard_label: str = field(default="title of dashboard")
    references_icon: str = field(default="list")
    sidemenu_icon: str = field(default="layout-text-window-reverse")

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
