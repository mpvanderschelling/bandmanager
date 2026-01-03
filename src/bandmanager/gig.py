#                                                                       Modules
# =============================================================================

# Standard
from datetime import datetime

# Local
from .client import Client
from .io import check_if_gig_exists
from .item import LineItems
from .show import Show
from .tech import TechnicalSpecs

# Third-party


#                                                        Authorship and Credits
# =============================================================================
__author__ = "Martin van der Schelling (martin@vanderschelling.com)"
__credits__ = ["Martin van der Schelling"]
__status__ = "Stable"
# =============================================================================
#
# =============================================================================


class Gig:
    def __init__(
        self,
        gig_name: str,
        id: int,
        line_items: LineItems,
        client: Client,
        show: Show,
        technical_specs: TechnicalSpecs,
    ):
        self.gig_name = gig_name
        self.line_items = line_items
        self.client = client
        self.show = show
        self.id = id
        self.technical_specs = technical_specs

    @classmethod
    def from_dict(cls, info_dict: dict):
        return cls(
            gig_name=info_dict["gig_name"],
            id=info_dict["id"],
            line_items=LineItems.from_list_of_dicts(info_dict["line_items"]),
            client=Client(**info_dict["client"]),
            show=Show(**info_dict["show"]),
            technical_specs=TechnicalSpecs(**info_dict["technical_specs"]),
        )

    def to_dict(self) -> dict:
        return {
            "gig_name": self.gig_name,
            "id": self.id,
            **self.client.to_dict(),
            **self.line_items.to_dict(),
            **self.show.to_dict(),
            **self.technical_specs.to_dict(),
        }


def create_id() -> str:
    # Get the current date
    current_date = datetime.now()

    # Format the date as YYYYmmdd
    formatted_date = current_date.strftime("%Y%m%d")

    index = 1
    while True:
        id = f"{formatted_date}{index:02}"
        if check_if_gig_exists(id):
            index += 1
        else:
            break
    return id
