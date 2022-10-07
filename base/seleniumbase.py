from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


# class seleniumbase(object):
class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 30, 0.3, ignored_exceptions = 'StaleElementReferenceException')

    # Типовые варианты поиска элементов на странице
    # # driver.implicitly_wait(10) # Варианта таймаута при обработке find_element ((
    # # find_element поиск элеиента на странице
    # element1 = driver.find_element(By.CSS_SELECTOR,'#id_123')
    # # вариант таймаута 15 с частотой проверки 0.3
    # wait = WebDriverWait(driver, 15, 0.3)
    # # ec.visibility_of_element_located поиск на странице и проверка Видимости''
    # element = wait.until(ec.visibility_of_element_located(By.CSS_SELECTOR, '#id_123')) # True or False

    # Адаптированный вариант поиска элементов без указания явного id

    # В случе, как сейчас, нужно функцию сделать приватной private чтобы она не была видна
    # другим классам перед неёй следует поставить два __
    # одно _ делает функцию protected  это те данные-члены класса, к которым можно получить
    # доступ внутри класса и классов, производных от этого класса.
    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME
                    }
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        # Возвроащать список строк веб элементов вебстраницы
        # Запись возвращаемого результата из функции можно записать...
        # element_list = []
        # for element in elements:
        #     element_list.append(element.text)
        # или же заменить более компактным запросом в виде [element.text for element in elements]
        return [element.text for element in elements]

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]
