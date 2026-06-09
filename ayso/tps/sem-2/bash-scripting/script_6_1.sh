#!/bin/bash

read -p "ingrese su nombre: " nombre;
read -p "ingrese su edad: " edad;

VOTING_AGE=16;

if [ $edad -gt $VOTING_AGE ]; then
    echo "Usted puede votar";
else
    echo "Usted no puede votar";
fi