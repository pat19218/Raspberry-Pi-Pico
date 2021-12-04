"""
File:        digital_OUT.py
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


led_placa = machine.Pin(25, machine.Pin.OUT) #machine.Pin(-numero de pin-, -entrada/salida-)
led1 = machine.Pin(1, machine.Pin.OUT)

while True:
    led_placa.value(1)  #Estado logico del pin (on/off)
    led1.value(1)
    utime.sleep(2)
    led_placa.value(0)
    led1.value(0)
    utime.sleep(2)
    
    led_placa.toggle()   #es com usar ~ en C, invierte el estado actual del pin
    led1.toggle()
    utime.sleep(0.25)
    led_placa.toggle()
    led1.toggle()
    utime.sleep(0.25)
    led_placa.toggle()
    led1.toggle()
    utime.sleep(0.25)
    led_placa.toggle()
    led1.toggle()
    utime.sleep(0.25)



