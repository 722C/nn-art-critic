#!/bin/bash

. ../bin/activate

echo "25% train 5% test"
python manage.py nn1 0.25 0.067
python manage.py nn1 0.25 0.067
python manage.py nn1 0.25 0.067
python manage.py nn1 0.25 0.067
python manage.py nn1 0.25 0.067
python manage.py nn1 0.25 0.067

echo "50% train 5% test"
python manage.py nn1 0.5 0.01
python manage.py nn1 0.5 0.01
python manage.py nn1 0.5 0.01
python manage.py nn1 0.5 0.01
python manage.py nn1 0.5 0.01
python manage.py nn1 0.5 0.01

echo "60% train 5% test"
python manage.py nn1 0.75 0.125
python manage.py nn1 0.75 0.125
python manage.py nn1 0.75 0.125
python manage.py nn1 0.75 0.125
python manage.py nn1 0.75 0.125
python manage.py nn1 0.75 0.125

echo "65% train 5% test"
python manage.py nn1 0.75 0.143
python manage.py nn1 0.75 0.143
python manage.py nn1 0.75 0.143
python manage.py nn1 0.75 0.143
python manage.py nn1 0.75 0.143
python manage.py nn1 0.75 0.143

echo "70% train 5% test"
python manage.py nn1 0.75 0.167
python manage.py nn1 0.75 0.167
python manage.py nn1 0.75 0.167
python manage.py nn1 0.75 0.167
python manage.py nn1 0.75 0.167
python manage.py nn1 0.75 0.167

echo "75% train 5% test"
python manage.py nn1 0.75 0.2
python manage.py nn1 0.75 0.2
python manage.py nn1 0.75 0.2
python manage.py nn1 0.75 0.2
python manage.py nn1 0.75 0.2
python manage.py nn1 0.75 0.2

echo "80% train 5% test"
python manage.py nn1 0.75 0.25
python manage.py nn1 0.75 0.25
python manage.py nn1 0.75 0.25
python manage.py nn1 0.75 0.25
python manage.py nn1 0.75 0.25
python manage.py nn1 0.75 0.25

echo "90% train 5% test"
python manage.py nn1 0.9 0.5
python manage.py nn1 0.9 0.5
python manage.py nn1 0.9 0.5
python manage.py nn1 0.9 0.5
python manage.py nn1 0.9 0.5
python manage.py nn1 0.9 0.5