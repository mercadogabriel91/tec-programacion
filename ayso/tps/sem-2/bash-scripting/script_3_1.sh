#!/bin/bash

read -p "Por favor ingrese su edad: " edad;

MAYORIA_DE_EDAD=18;

if [ $edad -ge $MAYORIA_DE_EDAD ]; then
    echo "Usted es mayor de edad";
else
    echo "Usted es menor de edad";
fi