
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys

from utils.retrieve_code import retrieve_phone_code


class UrbanRoutesPage:
# region SELECTORS

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_request_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    phone_number_button = (By.CSS_SELECTOR, '.np-button')
    phone_number_field = (By.ID, 'phone')
    phone_number_filled = (By.CSS_SELECTOR, '.np-text')
    phone_next_button = (By.CSS_SELECTOR, '.button.full')
    phone_code_field = (By.ID, 'code')
    phone_submit_button = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')
    credit_card_button = (By.XPATH, "//div[@class='pp-value-text']")
    credit_card_add_button = (By.XPATH, '//div[@class="pp-title" and text()="Agregar tarjeta"]')
    credit_card_number_field = (By.ID, 'number')
    credit_card_code_field = (By.CSS_SELECTOR, '#code.card-input')
    credit_card_submit_button = (By.XPATH, '//button[@class="button full" and text()="Agregar"]' )
    close_credit_card_form = (By.CSS_SELECTOR, '.payment-picker.open .section.active .close-button')
    payment_method_assert = (By.XPATH, "//div[@class='pp-value-text' and text()='Tarjeta']")
    message_driver_field = (By.ID, 'comment')
    blanket_napkins_switch = (By.XPATH, "//div[contains(@class, 'r-type-switch')][.//div[text()='Manta y pañuelos']]//span[contains(@class, 'slider')]")
    blanket_napkin_switch_assert = (By.XPATH,"//div[contains(@class, 'r')][.//div[contains(text(), 'Manta y pañuelos')]]//input[@type='checkbox']")
    icecream_counter = (By.XPATH, "//div[@class='counter-plus']")
    icecream_counter_value = (By.XPATH,"//div[contains(@class, 'counter-value')]")
    order_taxi_button = (By.XPATH, "//span[@class='smart-button-main' and text()='Pedir un taxi']")
    searching_driver = (By.XPATH,"//div[contains(@class, 'order-header-title') and text()='Buscar automóvil']")
    driver_found_order_number = (By.XPATH, "//div[@class='order-number']")
    driver_found_ETA = (By.XPATH, "//div[contains(@class, 'order-header-title')]")
    driver_found_cancel = (By.XPATH, "//div[@class='order-btn-group'][.//div[text()='Cancelar']]")
    driver_found_details = (By.XPATH, "//div[@class='order-btn-group'][.//div[text()='Detalles']]")
    driver_found_driver = (By.XPATH, "//div[@class='order-btn-group'][.//div[contains(@class, 'order-btn-rating')]]/div[2]")

# endregion

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.wait_driver = WebDriverWait(driver, 120)

# ============================ ROUTE ======================================
# region ROUTE

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

# endregion
# =============================TAXI REQUEST BUTTON ========================
# region TAXI REQUEST

    def get_taxi_request_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.taxi_request_button)
        )

    def click_taxi_request_button(self):
        self.get_taxi_request_button().click()

# endregion
# ============================ COMFORT ====================================
# region COMFORT

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
# ============================ PHONE NUMBER ===============================
# region Phone

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
            EC.element_to_be_clickable(self.phone_next_button)
        )
    def click_next_button(self):
        self.get_next_button().click()

    def get_code_field(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.phone_code_field)
        )
    def click_code_field(self):
        self.get_code_field().click()
    def set_code_field(self):
        self.wait.until(
            EC.visibility_of_element_located(self.phone_code_field)
        ).send_keys(retrieve_phone_code(self.driver))

    def get_submit_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.phone_submit_button)
        )
    def click_submit_button(self):
        self.get_submit_button().click()

# endregion
# ============================ Credit Card ================================
# region Credit_Card

    def get_creditcard_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.credit_card_button)
        )
    def click_creditcard_button(self):
        self.get_creditcard_button().click()

    def get_add_credit_card_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.credit_card_add_button)
        )
    def click_add_credit_card_button(self):
        self.get_add_credit_card_button().click()

    def set_add_credit_number_field(self, card_number):
        self.wait.until(
            EC.visibility_of_element_located(self.credit_card_number_field)
        ).send_keys(card_number)
    def set_add_credit_card_number_assert(self):
        return self.driver.find_element(*self.credit_card_number_field).get_property('value')

    def set_credit_card_code_field(self, card_code):
        self.wait.until(
            EC.visibility_of_element_located(self.credit_card_code_field)
        ).send_keys(card_code, Keys.TAB)
    def set_credit_card_code_assert(self):
        return self.driver.find_element(*self.credit_card_code_field).get_property('value')

    def get_submit_credit_card_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.credit_card_submit_button)
        )
    def click_submit_credit_card_button(self):
        self.get_submit_credit_card_button().click()

    def get_close_credit_card_button_form(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.close_credit_card_form)
        )
    def click_close_credit_card_button_form(self):
        self.get_close_credit_card_button_form().click()

    def set_payment_method_added_assert(self):
        return self.driver.find_element(*self.payment_method_assert).text

# endregion
# ============================ Message ====================================
# region MESSAGE

    def set_message_field(self, message):
       self.wait.until(
           EC.visibility_of_element_located(self.message_driver_field)
       ).send_keys(message)
    def get_message_field_assert(self):
        return self.driver.find_element(*self.message_driver_field).get_property('value')
    # endregion
# ============================ BLANKET & NAPKINS ==========================
#region B & N
    def get_blanket_napkin_switch(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.blanket_napkins_switch)
        )
    def click_blanket_napkin_switch(self):
        self.get_blanket_napkin_switch().click()

    def get_blanket_napkin_switch_assert(self):
        return self.driver.find_element(*self.blanket_napkin_switch_assert).is_selected()

    #endregion
# ============================ ICE CREAM ==================================
# region ICECREAM

    def get_icecream_counter_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.icecream_counter)
        )
    def click_icecream_counter_button(self, quantity):
        for _ in range(quantity):
            self.get_icecream_counter_button().click()

    def get_icecream_counter_value(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.icecream_counter_value)
        ).text

    #endregion
# ============================ SEARCHING DRIVER ===========================
# region SEARCHING

    def get_order_taxi_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.order_taxi_button)
        )

    def click_order_taxi_button(self):
        self.get_order_taxi_button().click()


    def get_searching_driver(self):
        return self.driver.find_element(*self.searching_driver).text

    def wait_driver_window(self):

        self.wait_driver.until(EC.visibility_of_element_located(self.driver_found_order_number))
        self.wait_driver.until(EC.visibility_of_element_located(self.driver_found_cancel))
        self.wait_driver.until(EC.visibility_of_element_located(self.driver_found_details))
        self.wait_driver.until(EC.visibility_of_element_located(self.driver_found_driver))
        self.wait_driver.until(EC.visibility_of_element_located(self.driver_found_ETA))


    def get_driver_found_order_number(self):
        value = self.driver.find_element(*self.driver_found_order_number).text.strip()
        print(f"Verificación número de orden: {value}")
        return value


    def get_driver_found_eta(self):
        value = self.driver.find_element(*self.driver_found_ETA).text.strip()
        print(f"Verificación ETA: {value}")
        return value


    def get_driver_found_cancel(self):
        value = self.driver.find_element(*self.driver_found_cancel).text.strip()
        print(f"Verificación botón cancelar: {value}")
        return value


    def get_driver_found_details(self):
        value = self.driver.find_element(*self.driver_found_details).text.strip()
        print(f"Verificación detalles: {value}")
        return value


    def get_driver_found_driver(self):
        value = self.driver.find_element(*self.driver_found_driver).text.strip()
        print(f"Verificación conductor: {value}")
        return value
    # endregion


