#                                                                       Modules
# =============================================================================

# Standard
import json

# Local
from .constants import JSON_FILES_FOLDER_NAME, ROOT_OUTPUT_DIR

# Third-party


#                                                        Authorship and Credits
# =============================================================================
__author__ = "Martin van der Schelling (martin@vanderschelling.com)"
__credits__ = ["Martin van der Schelling"]
__status__ = "Stable"
# =============================================================================
#
# =============================================================================


def save_json(info_dict: dict):
    # save info_dict to JSON file
    directory = ROOT_OUTPUT_DIR / JSON_FILES_FOLDER_NAME

    directory.mkdir(parents=True, exist_ok=True)

    filename = (directory / f"{info_dict['id']}").with_suffix(".json")

    # Save the dictionary to the JSON file
    with open(filename, "w") as json_file:
        json.dump(info_dict, json_file, indent=4)


def open_json(id: str) -> dict:
    # open the JSON file
    directory = ROOT_OUTPUT_DIR / JSON_FILES_FOLDER_NAME
    filename = (directory / id).with_suffix(".json")

    if not filename.exists():
        raise FileNotFoundError(f"File {filename} does not exist")

    with open(filename) as json_file:
        return json.load(json_file)


def check_if_gig_exists(id: str) -> bool:
    # open the JSON file
    directory = ROOT_OUTPUT_DIR / JSON_FILES_FOLDER_NAME
    filename = (directory / id).with_suffix(".json")

    return filename.exists()
