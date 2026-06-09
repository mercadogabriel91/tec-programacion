#!/bin/bash

PASSWORD="";

until [ $PASSWORD == "secreto" ]; do
    read -p "Ingrese la contraseña: " PASSWORD;
    if [ $PASSWORD != "secreto" ]; then
        echo "Contraseña incorrecta";
    else
        echo "Contraseña correcta";
        break;
    fi
done;