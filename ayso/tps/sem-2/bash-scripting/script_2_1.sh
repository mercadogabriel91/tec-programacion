#!/bin/bash

n_1=3;
n_2=6;

sum=$(($n_1 + $n_2));
sub=$(($n_1 - $n_2));
mul=$(($n_1 * $n_2));
div=$(($n_1 / $n_2));

echo "los numeros son $n_1 y $n_2";
echo "la suma es $sum";
echo "la resta es $sub";
echo "la multiplicacion es $mul";
echo "la division es $div";