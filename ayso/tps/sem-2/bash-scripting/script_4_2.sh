#!/bin/bash

MAX_RANGE=100;
COUNT=0;

while [ $COUNT -lt $MAX_RANGE ]; do
    ((COUNT ++));
done;

echo "El numero de iteraciones es $COUNT";