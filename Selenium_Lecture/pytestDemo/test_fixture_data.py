import pytest

# @pytest.mark.usefixtures("dataLoad")
class TestExample2:
    def test_editProfile(self, dataLoad):
        print(dataLoad)

def test_cross_browsing(crossBrowser):
    print(crossBrowser)