#!/usr/bin/env bash
#
#D Este script permite convertir de una moneda a otra.
#D
#D converter.sh COP USD # convierte de peso a dolar
#D converter.sh USD # convierte de dolar a peso
#
# El sitio desde donde se toma la informacion es APILayer.com.
# https://apilayer.com/marketplace/fixer-api#documentation-tab
#
#A Autor: John Sanabria - john.sanabria@correounivalle.edu.co
#F Fecha: 01-10-2023
#
. apilayer.key # <-- aqui se define la variable KEY
BASE="USD"
SYMBOLS="COP"
TMPFILE=$(mktemp)
if [ ! -z "${2}" ]; then
  SYMBOLS="${2}"
  if [ ! -z "${1}"]; then
    BASE="${1}"
  fi
fi
#echo "A convertir de ${BASE} a ${SYMBOLS}"
curl -s --request GET \
"https://api.apilayer.com/fixer/latest?base=${BASE}&symbols=${SYMBOLS}" \
--header "apikey: ${KEY}" > ${TMPFILE}
cat ${TMPFILE} | jq ".rates.${SYMBOLS}"
rm ${TMPFILE}
