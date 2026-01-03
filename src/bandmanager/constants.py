#                                                                       Modules
# =============================================================================

# Standard
from importlib.resources import files
from pathlib import Path

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


templates_dir = files("bandmanager").joinpath("templates")

PATH_TEMPLATES = Path(
    "/Users/martin/Documents/GitHub/bandmanager/src/bandmanager/templates"
)
VAT_LOW = 0.09
VAT_HIGH = 0.21
ROOT_OUTPUT_DIR = Path("/Users/martin/Documents/GitHub/bandmanager/output")
LIBREOFFICE_COMMAND = "soffice"
JSON_FILES_FOLDER_NAME = "json_files"
