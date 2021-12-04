"""
File:        digital_IN.py
Dispositivo: Raspberry Pi Pico -RP2040-
Autor:       Cristhofer Patzán
Compilador:  Thonny V3.3.13

Programa:    Syntaxis y comandos básicos
Hardware:    Raspberry Pi Pico -RP2040-
Creación:    3 de diciembre de 2021
modificado:  3 de diciembre de 2021
"""
import utime       #para delays
import machine     #Libreria que traduce python para cargar al uC
                   #Para saber funciones disponibles ingresar en la shell/consola --> help(machine)

                   #GPIO, entrada/output, PULL_DOWN/PULL_UP
button = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN) #Todos los GPIO tiene la resistencia para la conf.
led_placa = machine.Pin(25, machine.Pin.OUT)

while True:
    
    #print(button.value()) #imprimo el estado del push
    led_placa.value(button.value())
    utime.sleep(0.25)
    
    if button.value() == 1:
        print("Presionado")
    else:
        print("No presionado")

