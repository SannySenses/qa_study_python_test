from base.seleniumbase import SeleniumBase
from base.utils import Utils
from selenium.webdriver.remote.webelement import WebElement


class HomePageNav(SeleniumBase):
    def __init__(self, driver):
        # SeleniumBase().__init__(driver)
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>li'  # запрос с вэб страницы элементов по модулю
        self.NAV_LINK_TEXT = 'Women,Men,Kids,Home,Beauty,Shoes,Handbags,Jewelry,Furniture,Toys,Gifts,Trending,Sale'

    def get_nav_links(self) -> list[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header navigation links')

    def get_nav_link_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    # метод для возврата навигационного элемента
    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)
