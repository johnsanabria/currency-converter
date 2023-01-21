#!/usr/bin/env bash
#
#D Este script toma de un API REST el valor del dolar en pesos y se sube
#D dicho valor a una hoja de calculo en Google Sheets
#
#A Autor: John Sanabria - john.sanabria@gmail.com
#F Fecha: 10-01-2023
#
echo -n "Obteniendo el precio del dolar..."
valor=$(./converter.sh)
echo " \$${valor}"
echo -n "Subiendo dato a Google Sheets..."
./updateCOPUSD_GS.py ${valor}
echo " hecho!"
