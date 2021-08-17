import pytest
from BaseClass import BaseClass

# @pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editProfile(self, dataLoad):
        log = self.getLogger()
        log.info(dataLoad)
        # print(dataLoad)

def test_cross_browsing(crossBrowser):
    print(crossBrowser)