"""
File:        hello world.py
Dispositivo: Raspberry Pi Pico -RP2040-
Autor:       Cristhofer Patzán
Compilador:  Thonny V3.3.13

Programa:    Syntaxis y comandos básicos
Hardware:    Raspberry Pi Pico -RP2040-
Creación:    2 de diciembre de 2021
modificado:  2 de diciembre de 2021
"""
import utime    #para hacer delays en segundos, acepta decimales

print("Loop starting!")
while True:
    print("Loop running!")
    utime.sleep(0.5)       #cada medio segundo
print("Loop finished!")

