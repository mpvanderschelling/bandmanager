#                                                                       Modules
# =============================================================================

#                                                        Authorship and Credits
# =============================================================================
__author__ = "Martin van der Schelling (mpvanderschelling@gmail.com)"
__credits__ = ["Martin van der Schelling"]
__status__ = "Stable"
# =============================================================================
#
# =============================================================================


class TechnicalSpecs:
    def __init__(
        self, full_setup: bool, dj_set: bool, dj_furniture: bool = False
    ):
        self.full_setup = full_setup
        self.dj_set = dj_set
        self.dj_furniture = dj_furniture

    def create_dj_set_text(self) -> str:
        text = ""
        if self.dj_set:
            text = "De Artiest faciliteert een DJ-set \
                (2 x Pioneer CDJ-2000 NXS2 + 1 DJM-900 NXS2)."
        if self.dj_furniture:
            if text:
                text += " "
            text += "De Artiest faciliteert een DJ-meubel."
        return text

    def to_dict(self) -> dict:
        if self.full_setup:
            full_setup_text = "Artiest"
        else:
            full_setup_text = "Opdrachtgever"

        return {
            "full_setup": full_setup_text,
            "dj_set": self.create_dj_set_text(),
        }
