#                                                                       Modules
# =============================================================================

# Local
from .document import Document

#                                                        Authorship and Credits
# =============================================================================
__author__ = "Martin van der Schelling (mpvanderschelling@gmail.com)"
__credits__ = ["Martin van der Schelling"]
__status__ = "Stable"
# =============================================================================
#
# =============================================================================


class Invoice(Document):
    DOCUMENT_TYPE = ".ods"
    DOCUMENT_NAME = "Factuur"


class Quotation(Document):
    DOCUMENT_TYPE = ".ods"
    DOCUMENT_NAME = "Offerte"


class Contract(Document):
    DOCUMENT_TYPE = ".odt"
    DOCUMENT_NAME = "Contract"
