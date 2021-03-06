from workflow.workflow_component import AbstractWorkflowComponent
import logging
import urllib
from string import Template

logger = logging.getLogger(__name__)


class WWWDownloader(AbstractWorkflowComponent):

    def pre_invoke(self):
        self.hemisphere = "n"
        self.date = 20141130

    def invoke(self, context):
        """Download a file from FTP..."""
        try:
            path = Template(context[self.slots[0]]["uri"])
            fill_strings = {"hemisphere": self.hemisphere, "day": self.date}
            path = path.substitute(fill_strings)
            logger.info("Downloading {0}".format(path))
            print type(self)
            # urllib.urlretrieve(path, "/tmp/oi.nc")
        except Exception, e:
            raise e

    def post_invoke(self):
        pass
