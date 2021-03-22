from PageObjects.settings import SettingPage
import pytest


@pytest.mark.smoke
@pytest.mark.demo
@pytest.mark.usefixtures("open_app")
class TestSettingCase:

    def test_setting_swipe(self, open_app, number=4):
        SettingPage(open_app).open_setting(number)
        # try:
        #     assert
        # except:
        #     pass



