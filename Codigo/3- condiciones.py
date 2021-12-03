"""
File:        condiciones.py
Dispositivo: Raspberry Pi Pico -RP2040-
Autor:       Cristhofer Patzán
Compilador:  Thonny V3.3.13

Programa:    Syntaxis y comandos básicos
Hardware:    Raspberry Pi Pico -RP2040-
Creación:    2 de diciembre de 2021
modificado:  2 de diciembre de 2021
"""

user_name = input ("Cuál es tu nombre? ")

if user_name == "Tacu":  
    print("Eres la mera verga!")  
else:
    print("A ok!")

veamos = input("Como se llama superman? ")

while veamos != "Clark Kent":
    print("You are not Superman - try again!")
    veamos = input("What is his name? ")
print("You are Superman!")


