# from selenium.webdriver.common.by import By
import time

from selenium.common import NoSuchFrameException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import Any, Literal, Union, Callable, Tuple, TypeVar, List
from collections.abc import Iterable

# from urllib3.util import url


class Actions:
    def set_implicit_wait(self, timeout: int):
        self.driver.implicitly_wait(timeout)  # Set implicit wait to 10 seconds

    def wait_and_click_element(driver, timeout, by, value):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            element.click()
        except Exception as e:
            print(f"Error: {e}")
            # Handle the exception (e.g., log it or raise it)

    def wait_for_presence_of_element_located(driver, timeout, by, value):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except Exception as e:
            print(f"Error: {e}")

    def wait_for_element_to_be_clickable(driver, timeout, by, value):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
        except Exception as e:
            print(f"Error: {e}")

    def wait_for_visibility_of_element_located(self, timeout, by, value):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((by, value))
            )
        except Exception as e:
            print(f"Error: {e}")

    def wait_for_visibility_of_all_elements_located(driver, timeout, by, value):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_all_elements_located((by, value))
            )
        except Exception as e:
            print(f"Error: {e}")

    def wait_for_visibility(element: WebElement, timeout: int = 10) -> Union[False, WebElement]:
        """
            Waits for an element to become visible.
            :param element: WebElement object
            :param timeout: Maximum wait time in seconds (default is 10 seconds)
            :return: The visible WebElement or False if not found
            """
        try:
            wait = WebDriverWait(element._parent, timeout)
            return wait.until(EC.visibility_of(element))
        except Exception:
            return False

    def wait_for_alert_is_present(driver: WebDriver, timeout: int = 10) -> Union[Alert, Literal[False]]:
        """
        Waits for an alert to be present.
        :param driver: WebDriver object - Currently Edge driver is used
        :param timeout: Maximum wait time in seconds (default is 10 seconds)
        :return: The Alert object or False if no alert found
        """
        try:
            wait = WebDriverWait(driver, timeout)
            return wait.until(EC.alert_is_present())
        except Exception:
            return False

    def wait_for_invisibility_of_element(driver, timeout, by, value):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element((by, value))
            )
        except Exception as e:
            print(f"Error: {e}")

    def wait_for_invisibility_of_element_located(driver, timeout, by, value):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element_located((by, value))
            )
        except Exception as e:
            print(f"Error: {e}")

    def wait_for_element_located_to_be_selected(driver, timeout, by, value):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_located_to_be_selected((by, value))
            )
        except Exception as e:
            print(f"Error: {e}")

    # def wait_for_frame_to_be_available_and_switch_to_it(driver, timeout, by, value):
    #     try:
    #         element = WebDriverWait(driver, timeout).until(
    #             EC.frame_to_be_available_and_switch_to_it((by, value))
    #         )
    #     except Exception as e:
    #         print(f"Error: {e}")

    def frame_to_be_available_and_switch_to_it(locator: Union[Tuple[str, str], str]) -> Callable[[WebDriver], bool]:
        """An expectation for checking whether the given frame is available to
        switch to.

        If the frame is available it switches the given driver to the
        specified frame.
        """

        def _predicate(driver: WebDriver):
            try:
                if isinstance(locator, Iterable) and not isinstance(locator, str):
                    driver.switch_to.frame(driver.find_element(*locator))
                else:
                    driver.switch_to.frame(locator)
                return True
            except NoSuchFrameException:
                return False

        return _predicate

    def wait_for_presence_of_all_elements_located(driver, timeout, by, value):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
        except Exception as e:
            print(f"Error: {e}")

    def wait_for_text_in_element(self, locator: tuple[str, str], text: str, timeout: int = 10) -> bool:
        """
        Waits for the specified text to be present in the element.
        :param driver: WebDriver object
        :param locator: Tuple (By, value) representing the element locator
        :param text: Expected text to be present in the element
        :param timeout: Maximum wait time in seconds (default is 10 seconds)
        :return: True if text is present, False otherwise
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.text_to_be_present_in_element(locator, text))
        except Exception:
            return False

    def text_to_be_present_in_element(driver: WebDriver, locator: tuple[str, str], text: str,
                                      timeout: int = 10) -> bool:
        """
        Waits for the specified text to be present in the element identified by the given locator.
        :param driver: WebDriver instance
        :param locator: Tuple (By, value) representing the element locator
        :param text: Text to be present in the element
        :param timeout: Maximum time to wait (default is 10 seconds)
        :return: True if the text is present, False otherwise
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
            return True
        except Exception:
            return False

    def title_is(self, title: str) -> Callable[[WebDriver], bool]:
        """An expectation for checking the title of a page.
            title is the expected title, which must be an exact match returns
            True if the title matches, false otherwise.
            """

    # def _predicate(driver: WebDriver):
    #     return driver.title == title
    #     return _predicate

    def title_contains(self, title: str) -> Callable[[WebDriver], bool]:
        """An expectation for checking that the title contains a case-sensitive
        substring.

        title is the fragment of title expected returns True when the title
        matches, False otherwise
        """

        def _predicate(driver: WebDriver):
            return title in driver.title

        return _predicate

    def url_contains(self, url: str) -> Callable[[WebDriver], bool]:
        """An expectation for checking that the current url contains a case-sensitive substring.

        url is the fragment of url expected, returns True when the url
        matches, False otherwise
        """

    # def _predicate(driver: WebDriver):
    #     return url in driver.current_url
    #
    #     return _predicate

    def visibility_of_any_elements_located(self, locator: tuple[str, str], timeout: int = 10) -> List[WebElement]:
        """
        Waits for at least one element identified by the given locator to be visible.
        :param driver: WebDriver instance
        :param locator: Tuple (By, value) representing the element locator
        :param timeout: Maximum time to wait (default is 10 seconds)
        :return: List of visible WebElements (empty list if none are visible)
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_any_elements_located(locator)
            )
            return elements
        except Exception:
            return []

    # ------------------------------------ Custom Actions ------------------------------------#

    def __init__(self, driver):
        self.actions = ActionChains(driver)

    def custom_click(self, element):
        self.actions.click(on_element=element)

    def custom_double_click(self, element):
        self.actions.double_click(on_element=element)

    def send_keys_to_element(self, element, text):
        self.actions.click(on_element=element).send_keys(text).perform()

    def click_and_hold(self, on_element): #-> ActionChains:
        # action_chains = ActionChains(driver)
        if on_element:
            self.actions.click_and_hold(on_element).perform()
        else:
            self.actions.click_and_hold().perform()
        # return action_chains

    def move_to_element(self, element: WebElement):
        self.actions.move_to_element(element).perform()

    def move_to_element_with_offset(self, element: WebElement, xoffset: int, yoffset: int):
        self.actions.move_to_element_with_offset(element, xoffset, yoffset).perform()

    def context_click(self, element):
        self.actions.context_click(element).perform()

    def drag_and_drop(self, source: WebElement, target: WebElement):
        self.actions.drag_and_drop(source, target).perform()

    def drag_and_drop_by_offset(self, source: WebElement, xoffset: int, yoffset: int):
        self.actions.drag_and_drop_by_offset(source, xoffset, yoffset).perform()

    def key_down(self, value: str, element: WebElement = None):
        if element:
            self.actions.key_down(value, element).perform()
        else:
            self.actions.key_down(value).perform()

    def key_up(self, value: str, element: WebElement = None):
        if element:
            self.actions.key_up(value, element).perform()
        else:
            self.actions.key_up(value).perform()

    def release(self, on_element: WebElement = None):
        if on_element:
            self.actions.release(on_element).perform()
        else:
            self.actions.release().perform()

    def pause(self, seconds: float | int):
        time.sleep(seconds)

    def scroll_to_element(self, element: WebElement):
        # actions = ActionChains(self.driver)
        self.actions.move_to_element(element)
        self.actions.perform()
