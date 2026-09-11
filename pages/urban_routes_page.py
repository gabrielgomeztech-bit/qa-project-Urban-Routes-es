
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.retrieve_code import retrieve_phone_code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_request_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    phone_number_button = (By.CSS_SELECTOR, '.np-button')
    phone_number_field = (By.ID, 'phone')
    phone_number_filled = (By.CSS_SELECTOR, '.np-text')
    next_button = (By.CSS_SELECTOR, '.button.full')
    code_field = (By.ID, 'code')
    submit_button = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
# region DONE
# =============================== ROUTE ===============================

    def set_from(self, from_address):
        self.wait.until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

# =============================== TAXI REQUEST BUTTON ===============================
    def get_taxi_request_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.taxi_request_button)
        )

    def click_taxi_request_button(self):
        self.get_taxi_request_button().click()

# =============================== COMFORT ===============================

    def get_comfort_icon(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_icon_assert(self):
        return self.wait.until(
            EC.presence_of_element_located(self.comfort_icon_assert)
        )
# endregion
# =============================== PHONE NUMBER ===============================

    def get_phone_number_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.phone_number_button)
        )

    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def set_phone_number_field(self, phone_number):
            self.wait.until(
                EC.visibility_of_element_located(self.phone_number_field)
            ).send_keys(phone_number)

    def get_phone_number_assert(self):
            return self.driver.find_element(*self.phone_number_field).get_property('value')

    def get_next_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.next_button)
        )
    def click_next_button(self):
        self.get_next_button().click()

    def get_code_field(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.code_field)
        )

    def click_code_field(self):
        self.get_code_field().click()

    def set_code_field(self):
        self.wait.until(
            EC.visibility_of_element_located(self.code_field)
        ).send_keys(retrieve_phone_code(self.driver))

    def get_submit_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.submit_button)
        )
    def click_submit_button(self):
        self.get_submit_button().click()





# =============================== Credit Card ===============================


