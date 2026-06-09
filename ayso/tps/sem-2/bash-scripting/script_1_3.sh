#!/bin/bash

BACKUP_DIR="backup";

mkdir -p $BACKUP_DIR;

touch "test.txt";

cp *.txt $BACKUP_DIR;