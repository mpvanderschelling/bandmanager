#                                                                       Modules
# =============================================================================

# Standard
from typing import Optional

# Third-party

# Local

#                                                        Authorship and Credits
# =============================================================================
__author__ = "Martin van der Schelling (martin@vanderschelling.com)"
__credits__ = ["Martin van der Schelling"]
__status__ = "Stable"
# =============================================================================
#
# =============================================================================


class Client:
    def __init__(
        self,
        name: str,
        address: Optional[str] = None,
        zipcode: Optional[str] = None,
        email: Optional[str] = None,
    ):
        self.name = name
        self.address = address
        self.zipcode = zipcode
        self.email = email

    def to_dict(self) -> dict:
        return self.__dict__
