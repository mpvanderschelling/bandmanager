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


templates_dir = files("dkb_management").joinpath("templates")

PATH_TEMPLATES = Path(
    "/Users/martin/Documents/GitHub/dkb_management/src/dkb_management/templates"
)
VAT_LOW = 0.09
VAT_HIGH = 0.21
ROOT_OUTPUT_DIR = Path("/Users/martin/Documents/GitHub/dkb_management/output")
LIBREOFFICE_COMMAND = "soffice"
JSON_FILES_FOLDER_NAME = "json_files"

# BASE_DIR = Path(__file__).resolve()
# api_key_file = BASE_DIR / "api_key.txt"

# open and save the api key
API_KEY = "AIzaSyC3mZx82tDiXQw9SsIIctJvBhnwx_I7BpY"
# with open(api_key_file, 'r') as f:
#     API_KEY = f.read().strip()
