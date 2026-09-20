import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from data import data
from pages.urban_routes_page import UrbanRoutesPage

class TestUrbanRoutes:

    def setup_method(self):
        options = Options()
        options.set_capability("goog:loggingPrefs",{'performance':'ALL'})
        self.driver = webdriver.Chrome(service=Service(), options=options)
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

# ================================= Steps =================================

    def set_route_and_order(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_taxi_request_button()
        self.routes_page.click_comfort_icon()

    def set_phone_number(self):
        self.routes_page.click_phone_number_button()
        self.routes_page.set_phone_number_field(data.phone_number)
        self.routes_page.click_next_button()
        self.routes_page.set_code_field()
        self.routes_page.click_submit_button()

    def add_creditcard(self):
        self.routes_page.click_creditcard_button()
        self.routes_page.click_add_credit_card_button()
        self.routes_page.set_add_credit_number_field(data.card_number)
        self.routes_page.set_credit_card_code_field(data.card_code)
        self.routes_page.click_submit_credit_card_button()
        self.routes_page.click_close_credit_card_button_form()

    def message_driver(self):
        self.routes_page.set_message_field(data.message_for_driver)

    def req_blanket_and_napkin(self):
        self.routes_page.click_blanket_napkin_switch()

    def get_n_icecream(self):
        self.routes_page.click_icecream_counter_button(2)

    def complete_taxi_order_flow(self):
        self.set_route_and_order()
        self.set_phone_number()
        self.add_creditcard()
        self.message_driver()
        self.req_blanket_and_napkin()
        self.get_n_icecream()
        self.routes_page.click_order_taxi_button()

    def wait_driver_window(self):
        self.routes_page.get_driver_found_order_number()
        self.routes_page.get_driver_found_eta()
        self.routes_page.get_driver_found_cancel()
        self.routes_page.get_driver_found_details()
        self.routes_page.get_driver_found_driver()



    def test_1_set_route(self):
        self.routes_page.set_route(data.address_from, data.address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_2_select_comfort_tariff(self):
        self.set_route_and_order()
        comfort_tariff = self.routes_page.get_comfort_icon_assert().text
        assert comfort_tariff == 'Comfort'

    def test_3_phone_number(self):
        self.set_route_and_order()
        self.set_phone_number()
        assert self.routes_page.get_phone_number_assert() == data.phone_number

    def test_4_add_creditcard(self):
        self.set_route_and_order()
        self.set_phone_number()
        self.add_creditcard()
        assert self.routes_page.set_payment_method_added_assert() == 'Tarjeta'

    def test_5_message_driver(self):
        self.set_route_and_order()
        self.message_driver()
        assert self.routes_page.get_message_field_assert() == data.message_for_driver

    def test_6_blanket_and_napkin(self):
        self.set_route_and_order()
        self.req_blanket_and_napkin()
        assert self.routes_page.get_blanket_napkin_switch_assert() is True

    def test_7_order_2_icecream(self):
        self.set_route_and_order()
        self.get_n_icecream()
        assert self.routes_page.get_icecream_counter_value() == "2"

    def test_8_taxi_order_window(self):
        self.set_route_and_order()
        self.set_phone_number()
        self.add_creditcard()
        self.message_driver()
        self.req_blanket_and_napkin()
        self.get_n_icecream()
        self.routes_page.click_order_taxi_button()
        assert self.routes_page.get_searching_driver() == "Buscar automóvil"


    def test_9_taxi_driver_assign(self):
        self.complete_taxi_order_flow()
        self.routes_page.wait_driver_window()

        assert self.routes_page.get_driver_found_order_number() != ""
        assert self.routes_page.get_driver_found_eta() != ""
        assert self.routes_page.get_driver_found_cancel() != ""
        assert self.routes_page.get_driver_found_details() != ""
        assert self.routes_page.get_driver_found_driver() != ""


    def teardown_method(self):
        self.driver.quit()

