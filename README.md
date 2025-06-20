# QA Tests

Este repositorio contiene las dos pruebas solicitadas para QA.

-----------------------------------------------

## Requisitos

* Sistema operativo Windows 10 o superior
* Administrador de entornos de desarrollo [Conda](https://www.anaconda.com/download/success)
* Navegador [Google Chrome](https://www.google.com/intl/es_mx/chrome/)
* La versión para Windows (win64) de [Chromedriver](https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.119/win64/chromedriver-win64.zip)
* El editor de texto que más te agrade
* To-Do: Versión para Firefox y para Linux

## Instalación

El ejecutable WebDriver **chromedriver** debe estar ubicado en 

```bash
C:\Webdriver
```

Esta ubicación puede ser variada pero require la modificación de la variable

```bash
driver_path
```

dentro del modulo 

```bash
testingyes.testingyes
```

Desde la raíz de la carpeta de este proyecto, con Conda, instala el entorno usando 


```bash
conda env create -f env.yml
```

## Uso

Para **[testingyes](http://www.testingyes.com/onlineshop/)**

Con el entorno activado en tu editor de textos favorito, ejecuta el script **test_testingyes_login.py**. Este script contiene las pruebas automáticas en lo que se refiere a login y creación de cuenta.

Del mismo modo, ejecuta el script **test_testingyes_cart.py** para realizar las pruebas del carrito.

Ambos archivos instancian un objeto **Testingyes()** como un bot que empieza a realizar las pruebas.
