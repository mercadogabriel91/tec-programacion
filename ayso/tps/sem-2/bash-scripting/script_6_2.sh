#!/bin/bash

LISTA_DE_NOMBRES=("Gabriel" "Emiliano" "Pedro" "Violeta");
touch "lista_de_nombres.txt";

for nombre in ${LISTA_DE_NOMBRES[@]}; do
   echo $nombre >> "lista_de_nombres.txt";
   echo "Hola! bienvenido a la lista $nombre";
done;
