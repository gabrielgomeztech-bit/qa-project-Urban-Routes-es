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

    def test_1_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to

    def test_2_select_comfort_tariff(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_taxi_request_button()
        self.routes_page.click_comfort_icon()

        comfort_tarif = self.routes_page.get_comfort_icon_assert().text
        assert comfort_tarif == 'Comfort'

    def test_3_phone_number(self):
        phone_number = data.phone_number
        self.routes_page.set_route(data.address_from, data.address_to)
        self.routes_page.click_taxi_request_button()
        self.routes_page.click_phone_number_button()
        self.routes_page.set_phone_number_field(phone_number)
        self.routes_page.click_next_button()
        self.routes_page.set_code_field()
        self.routes_page.click_submit_button()
        assert self.routes_page.get_phone_number_assert() == data.phone_number


    def teardown_method(self):
        self.driver.quit()
