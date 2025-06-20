import amazon.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
import time

logger = logging.getLogger(__name__)
logging.basicConfig(filename='amazon.log', level=logging.INFO)


class Amazon(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Webdriver",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Amazon, self).__init__()
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

    def extender_categorias(self):
        more_element = self.find_element(
            By.CLASS_NAME, "a-size-base.a-link-normal")
        more_element.click()

        time.sleep(5)
