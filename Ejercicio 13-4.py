#!/user/bin/python
# -*- coding: utf-8 -*-

fichero = open("/etc/passwd", "r")
lista = fichero.readlines()
fichero.close()
for linea in lista:
    print "Usuario: " + linea.split(":")[0] + " Consola: " + linea.split(":")[6]
print "Total de usuarios: " + str(len(lista))
