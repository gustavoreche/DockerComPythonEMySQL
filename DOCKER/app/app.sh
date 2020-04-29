#!/bin/sh

pip install --upgrade pip
pip install bottle==0.12.13 mysql-connector-python==8.0.13 redis==2.10.5
python -u enviador.py