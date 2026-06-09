#!/bin/bash

numbers_list=(4 6 8 9 6);
sum=0;

for number in ${numbers_list[@]}; do
    sum=$((sum + number));
done;

length=${#numbers_list[@]};
average=$((sum / length));

echo "La suma de los numeros es $sum";
echo "El promedio de los numeros es $average";