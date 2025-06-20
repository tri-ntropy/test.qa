import testingyes.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
import time

logger = logging.getLogger(__name__)
logging.basicConfig(filename='testingeyes.log', level=logging.INFO)


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
        logger.info('Metodo: abrir_pagina. Abre pagina principal')

    def clic_sigin(self):
        sigin_element = self.find_element(By.ID, "_desktop_user_info")
        sigin_element.click()
        print("========================")
        print("Exito: Se abrió el sigin")
        print("========================")
        logger.info('Metodo: clic_sigin. Abre pagina para loggearse')

    def crear_cuenta(self, firstname, lastname, email, password):
        logger.info('Metodo: crear_cuenta. Iniciando creacion de cuenta')
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

        print("========================")
        print("Exito: Se creó la cuenta")
        print("========================")
        logger.info(
            rf'Metodo: crear_cuenta. Exito: "{firstname}", "{lastname}", y "{email}" son validos. Cuenta creada'
        )
        time.sleep(5)

    def loggear_cuenta(self, email, password):
        email_element = self.find_element(By.CLASS_NAME,
                                          "form-control")
        email_element.send_keys(email + Keys.ENTER)

        password_element = self.find_element(By.CLASS_NAME,
                                             "form-control.js-child-focus.js-visible-password")
        password_element.click()
        password_element.send_keys(password + Keys.ENTER)

        print("=========================")
        print("Exito: Se loggeo la cuenta")
        print("=========================")
        logger.info(
            rf'Metodo: loggear_cuenta. Exito: Se loggeo la cuenta con el email "{email}", y password "{password}"'
        )

    def agregar_producto_carrito(self, n):
        product_element = self.find_element(
            By.XPATH, "/html/body/main/section/div/div/section/section/section/div/article[2]"
        )
        product_element.click()

        quantity_element = self.find_element(By.ID, "quantity_wanted")
        quantity_element.click()
        quantity_element.clear()
        quantity_element.send_keys(n)

        add_element = self.find_element(
            By.CLASS_NAME, "btn.btn-primary.add-to-cart")
        add_element.click()

        WebDriverWait(self, 10).until(
            EC.element_to_be_clickable((By.ID, "blockcart-modal")))

        end_add_element = self.find_element(
            By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[2]/div/div/a")
        end_add_element.click()

        print("====================================")
        print(f"Exito: Se agregaron los {n} productos")
        print("====================================")

        logger.info(
            rf'Metodo: agregar_producto_carrito. Exito: Se agregaron {n} productos"'
        )

    def quitar_producto_carrito(self):
        product_element = self.find_element(
            By.CLASS_NAME, "remove-from-cart"
        )
        product_element.click()

        time.sleep(10)

        print("=================================")
        print(f"Exito: Se quitaron los productos")
        print("=================================")

        logger.info(
            rf'Metodo: quitar_producto_carrito. Exito: Se quitaron los productos del carrito"'
        )
