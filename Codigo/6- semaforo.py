"""
File:        semaforo.py
Dispositivo: Raspberry Pi Pico -RP2040-
Autor:       Cristhofer Patzán
Compilador:  Thonny V3.3.13

Programa:    Syntaxis y comandos básicos
Hardware:    Raspberry Pi Pico -RP2040- , leds, buzzer, resistencia, push button
Creación:    6 de diciembre de 2021
modificado:  6 de diciembre de 2021
"""
import utime       #para delays
import machine     #Libreria que traduce python para cargar al uC
                   #Para saber funciones disponibles ingresar en la shell/consola --> help(machine)
import _thread     #Me permite realizar trabajo en paralelo, a cada proceso de estos se le llama
                   #hilos o subprocesos. Es similar a ejecutar varios programas diferentes al mismo tiempo
                   #https://python-para-impacientes.blogspot.com/2016/12/threading-programacion-con-hilos-i.html

led_red = machine.Pin(19, machine.Pin.OUT)
led_amber = machine.Pin(17, machine.Pin.OUT)
led_green = machine.Pin(16, machine.Pin.OUT)
buzzer = machine.Pin(18, machine.Pin.OUT)
button = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)




