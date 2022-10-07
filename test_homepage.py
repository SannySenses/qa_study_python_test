import time
import pytest
from pom.homepage_nav import HomePageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:
    # def test_homepage(self):
    #      pass

    def test_nav_links(self):
        homepage_nav = HomePageNav(self.driver)
        actual_links = homepage_nav.get_nav_link_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        print(homepage_nav.get_nav_link_text())
        assert expected_links == actual_links, "Validating Nav Links text"
        elements = homepage_nav.get_nav_links()
        #        homepage_nav.get_nav_link_by_name('Beauty').click()
        # for element in elements:
        #     element.click()
        #
        #     time.sleep(3)
        for index in range(13):
            homepage_nav.get_nav_links()[index].click()
            homepage_nav.driver.delete_all_cookies()
            time.sleep(5)