#!/usr/bin/env python3
#
#D Este script permite actualizar el valor del dolar en una hoja de cálculo
#D de Google Sheets
#
# Este script se apoya en la libreria 'gspread'
# https://github.com/burnash/gspread
#
#A Autor: John Sanabria - john.sanabria@gmail.com
#F Fecha: 10-01-2023
#
import datetime
import gspread
import sys

#
# 'Constantes'
#
cellRef = 'A1'
gsName = 'COP_USD'

#
# Funciones Utilitarias para obtener y modificar valores
#
# Lo que se devuelve despues de leer una celda de una hoja de calculo en
# Google Sheets es una lista de listas. Por eso se obtiene de la primera lista
# el primer elemento, cellVal[0][0]
#
# El valor que se obtiene es de la forma 'A-2'. Por eso se hace el split por 
# el simbolo '-'.
#
def getCol(cellVal):
  return cellVal[0][0].split('-')[0]

def getRow(cellVal):
  return cellVal[0][0].split('-')[1]

#
# 'val' es una cadena que representa un caracter y por eso se hace toda esta 
# gestion del dato.
# Como hacer esto se encontro en este sitio
# https://stackoverflow.com/questions/4179176/python-incrementing-a-character-string
#
def incCol(val):
  return chr(ord(val) + 1)

#
# Las filas en las hojas de calculo estan numeradas de 1, 2, 3,... Sin embargo,
# a la hora de usar ese valor para actualizar una celda en la hoja de calculo 
# se debe usar la representacion en cadena (str) de ese numero
#
def incRow(val):
  val = int(val) + 1
  return str(val)

# ----
#
# Funciones que actualizan datos en las hojas de calculo en Google Sheets
#
def actualizarValCOPUSD(sh, col, row, valorCOP):
  sh.sheet1.update(col + row,valorCOP)
  
def actualizarFecha(sh, col, row):
  sh.sheet1.update( incCol(col) + row, str(datetime.datetime.now()) )

def actualizarRef(sh, col,row):
  sh.sheet1.update(cellRef, col + '-' + incRow(row))

# ---
# La funcion 'main'
#
def main():
  if len(sys.argv) != 2:
    print("Se requiere valor del dolar en pesos")
    sys.exit(1)
  valorCOP = sys.argv[1]
  gc = gspread.service_account()
  sh = gc.open(gsName)
  # Aqui se consigue el valor en donde se debe almacnear el valor
  # obtenido del dolar
  cell_ref = sh.sheet1.get(cellRef)
  col = getCol(cell_ref)
  row = getRow(cell_ref)
  
  actualizarValCOPUSD(sh, col, row, valorCOP)
  actualizarFecha(sh, col, row)
  actualizarRef(sh, col, row)

if __name__ == '__main__':
  main()
