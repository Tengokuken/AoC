#!/bin/bash
start=1
while [[ $start -le 25 ]]
do
	mkdir "day"$start
	touch "day"$start/"day"$start.py
	((start++))
done
echo All gucci
