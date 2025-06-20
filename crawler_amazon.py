from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = webdriver.ChromeService(executable_path="resources/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb")


# Espera a que el botón o la lista esté disponible y haz clic para expandir
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(3)
boton_more = wait.until(EC.element_to_be_clickable(
    (By.CLASS_NAME, "SeeMoreButton-module__container_j2YuDOVGk8QHFxg6xPQk")))

boton_more.click()

categorias = wait.until(EC.presence_of_all_elements_located(
    (By.CLASS_NAME, "a-size-base.a-color-base")))

categorias_reales = [(i, i.text)
                     for i in categorias
                     if i.text not in [
                         "Categoría", "Todo", "Marcas", "Ring", "Bedsure", "SAUKOLE",
                         "HYSEYY", "Opinión del cliente", "Precio", "Por menos de US$25",
                         "Por menos de US$50", "Por menos de US$100", "Por menos de US$200",
                         "US$200 en adelante", "Descuento", r"10% de descuento o más",
                         r"25% de descuento o más", r"50% de descuento o más",
                         r"70% de descuento o más", "Programas de Prime", "Exclusivo de Prime",
                         "eufy", "In The Swim", "Amazon", "Best Choice Products", "MCGOR",
                         "Acceso prioritario con Prime"]
                     ]

datos = dict()

for cat in categorias_reales:
    datos[cat[1]] = []
    try:
        print(cat[1])

        cat[0].click()
        productos = driver.find_elements(
            By.CLASS_NAME, "a-section.a-spacing-none.ProductCardImage-module__wrapper_YgLz4kq6ekChj01qeqOf")
        productos_nombres = [p.text for p in productos]
        print(productos_nombres)
        datos[cat[1]] = productos_nombres
    except:
        continue

    delfilter_element = driver.find_element(
        By.CLASS_NAME, "a-size-base.a-link-normal")
    delfilter_element.click()

time.sleep(190)

# Ahora espera a que aparezcan los elementos de la lista expandida
# categorias = wait.until(EC.presence_of_all_elements_located(
#    (By.CSS_SELECTOR, ".clase-de-las-categorias")))

# Extrae el texto de cada categoría
# for categoria in categorias:
#    print(categoria.text)

driver.quit()
# with Amazon() as bot:
#    bot.abrir_pagina()
#    bot.extender_categorias()
