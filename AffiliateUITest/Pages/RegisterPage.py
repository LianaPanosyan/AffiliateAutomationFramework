from AffiliateUITest.Helpers.BasicHelper import BasicHelper
from selenium.webdriver.common.by import By
import logging


class RegisterPage(BasicHelper):
    email_field = (By.ID, 'email')
    new_password_filed = (By.ID, 'password')
    confirm_password_filed = (By.ID, 'confirmPassword')
    select_currency_field = (By.XPATH, '//input[@placeholder="* Select Currency"]')
    select_code_field = (By.XPATH, '//input[@placeholder="Select"]')
    mobile_field = (By.ID, 'phoneNumber')
    username_field = (By.ID, 'username')
    birth_date_field = (By.ID, 'birthday')
    first_name_field = (By.ID, 'name')
    cpf_number_field = (By.ID, 'cpfNumber')
    telegram_field = (By.ID, 'telegram')
    marketing_website_field = (By.ID, 'marketingWebsite')
    countries_field = (By.XPATH, '//input[@placeholder="Countries"]')
    last_name_field = (By.ID, 'lastName')
    second_last_name_field = (By.ID, 'secondLastName')
    address_field = (By.ID, 'secondName')
    company_name_field = (By.ID, 'companyName')
    city_field = (By.ID, 'city')
    skype_field = (By.ID, 'skype')
    zip_code_field = (By.ID, 'zipCode')
    gender_field = (By.XPATH, '//input[@placeholder="Gender"]')
    accept_terms_checkbox = (By.XPATH, '//label[@class="checkbox cr-element s-small"]')
    sign_up_button = (By.XPATH, '//span[@class="ellipsis-text" and text()="Sign Up"]')
    usd_currency = (By.XPATH, '//p[@title="USD"]')

    def register_user(self, email, new_password, confirm_password):
        self.find_and_send_keys(self.email_field, email)
        self.find_and_send_keys(self.new_password_filed, new_password)
        self.find_and_send_keys(self.confirm_password_filed, confirm_password)
        self.find_and_click(self.select_currency_field)
        self.find_and_click(self.usd_currency)
        self.find_and_click(self.sign_up_button)
