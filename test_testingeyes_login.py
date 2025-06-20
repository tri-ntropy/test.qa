from testingyes.testingyes import Testingyes

firstname = "Janxzyab[]x"
lastname = "Dozyab!!x"
email = "mipruebayxzwab°bxy@email.com"
password = "asdfqwer1234x"
cuenta_nueva = True
cuenta_creada = True
if cuenta_nueva:
    cuenta_creada = False

with Testingyes() as bot:
    bot.abrir_pagina()
    bot.clic_sigin()
    if cuenta_nueva:
        bot.crear_cuenta(firstname=firstname,
                         lastname=lastname,
                         email=email,
                         password=password)
    if cuenta_creada:
        bot.loggear_cuenta(email, password)
