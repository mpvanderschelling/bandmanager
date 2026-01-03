#                                                                       Modules
# =============================================================================

# Standard
import subprocess

# Third-party
from relatorio.templates.base import RelatorioStream
from relatorio.templates.opendocument import Template

# Local
from ..constants import LIBREOFFICE_COMMAND, PATH_TEMPLATES, ROOT_OUTPUT_DIR
from ..gig import Gig

#                                                        Authorship and Credits
# =============================================================================
__author__ = "Martin van der Schelling (martin@vanderschelling.com)"
__credits__ = ["Martin van der Schelling"]
__status__ = "Stable"
# =============================================================================
#
# =============================================================================


class Document:
    DOCUMENT_TYPE = ".ods"
    DOCUMENT_NAME = "Document"

    def __init__(self, gig: Gig):
        self.gig = gig

        folder_name = f"{gig.show.date.strftime('%Y%m%d')}_{gig.gig_name}"
        self.directory = ROOT_OUTPUT_DIR / folder_name / f"{self.gig.id}"

        self.name = (
            f"{self.gig.id} {self.DOCUMENT_NAME} De Klittenband "
            f"- {self.gig.gig_name}"
        )

    def generate(self) -> RelatorioStream:
        template_file = (PATH_TEMPLATES / self.DOCUMENT_NAME).with_suffix(
            self.DOCUMENT_TYPE
        )

        document = Template(source="", filepath=template_file)
        return document.generate(o=self.gig.to_dict()).render()

    def write(self, relatorio_stream: RelatorioStream):
        (self.directory).mkdir(parents=True, exist_ok=True)

        with open(
            (self.directory / self.name).with_suffix(self.DOCUMENT_TYPE), "wb"
        ) as f:
            f.write(relatorio_stream.getvalue())

    def run(self):
        self.write(self.generate())
        self.create_pdf()

    def create_pdf(self):
        command = (
            f"{LIBREOFFICE_COMMAND} --headless --convert-to pdf "
            f'--outdir "{self.directory}" '
            f'"{(self.directory / self.name).with_suffix(self.DOCUMENT_TYPE)}"'
        )

        # Execute the command
        _ = subprocess.run(  # noqa
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
