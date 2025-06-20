from testingyes.testingyes import Testingyes

n = -1

with Testingyes() as bot:
    bot.abrir_pagina()
    bot.agregar_producto_carrito(n)
    bot.quitar_producto_carrito()
