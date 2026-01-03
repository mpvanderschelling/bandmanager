#                                                                       Modules
# =============================================================================

# Standard
from datetime import datetime
from typing import Optional

# Third-party

# Local

#                                                        Authorship and Credits
# =============================================================================
__author__ = "Martin van der Schelling (mpvanderschelling@gmail.com)"
__credits__ = ["Martin van der Schelling"]
__status__ = "Stable"
# =============================================================================
#
# =============================================================================


class Show:
    def __init__(
        self,
        date: str,
        location: Optional[str] = None,
        starting_time: Optional[str] = None,
        duration: Optional[str] = None,
    ):
        self.location = location
        self.date = datetime.strptime(date, "%d-%m-%Y")
        self.starting_time = starting_time
        self.duration = duration

    def to_dict(self) -> dict:
        starting_time_text = (
            self.starting_time if self.starting_time else "nnb"
        )
        duration_text = self.duration if self.duration else "nnb"
        location_text = self.location if self.location else "nnb"

        return {
            "location": location_text,
            "date": self.date.strftime("%d %B %Y"),
            "starting_time": starting_time_text,
            "duration": duration_text,
        }
