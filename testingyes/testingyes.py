import testingyes.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


class Testingyes(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Webdriver",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Testingyes, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def abrir_pagina(self):
        self.get(const.BASE_URL)
        print("=========================")
        print("Exito: Se abrió la página")
        print("=========================")

    def clic_sigin(self):
        sigin_element = self.find_element(By.ID, "_desktop_user_info")
        sigin_element.click()
        print("========================")
        print("Exito: Se abrió el sigin")
        print("========================")

    def crear_cuenta(self, firstname, lastname, email, password):
        noaccount_element = self.find_element(By.CLASS_NAME, "no-account")
        noaccount_element.click()

        gender_element = self.find_element(By.CLASS_NAME, "custom-radio")
        gender_element.click()

        firstname_element = self.find_element(By.NAME, "firstname")
        firstname_element.send_keys(firstname + Keys.ENTER)

        lastname_element = self.find_element(By.NAME, "lastname")
        lastname_element.send_keys(lastname + Keys.ENTER)

        email_element = self.find_element(By.NAME, "email")
        email_element.send_keys(email + Keys.ENTER)

        password_element = self.find_element(By.NAME, "password")
        password_element.send_keys(password + Keys.ENTER)

        optin_element = self.find_element(By.NAME, "optin")
        optin_element.click()

        newsletter_element = self.find_element(By.NAME, "newsletter")
        newsletter_element.click()

        agreement_element = self.find_element(By.NAME, "psgdpr")
        agreement_element.click()

        save_element = self.find_element(
            By.CLASS_NAME,
            "btn.btn-primary.form-control-submit.float-xs-right")
        save_element.click()

        try:
            help_elements = list(self.find_elements(
                By.CLASS_NAME, "help-block"))
            if len(help_elements) > 0:
                print("XXXXXXXXXXXXXXXXXXXXXXXX")
                print(
                    f"Error: {firstname}, {lastname}, y/o {email} incluyen carácteres no válidos"
                )
                print("XXXXXXXXXXXXXXXXXXXXXXXX")
        except:
            print("========================")
            print("Exito: Se creó la cuenta")
            print("========================")

    def loggear_cuenta(self, email, password):
        email_element = self.find_element(By.CLASS_NAME,
                                          "form-control")
        email_element.send_keys(email + Keys.ENTER)

        password_element = self.find_element(By.CLASS_NAME,
                                             "form-control.js-child-focus.js-visible-password")
        password_element.click()
        password_element.send_keys(password + Keys.ENTER)

        print("=========================")
        print("Exito: Se loggeó la cuenta")
        print("=========================")
