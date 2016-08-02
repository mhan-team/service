#!/bin/sh
mysql -u root -p$SQL_PASSWORD -e "drop database followme"
mysql -u root -p$SQL_PASSWORD -e  "create database followme"
rm followme/migrations/*_initial.py
python3 manage.py migrate
python3 manage.py makemigrations followme
python3 manage.py sqlmigrate followme 0001
bold=$(tput bold)
normal=$(tput sgr0)
python3 manage.py migrate
echo "${bold}When prompted enter email and password for the admin user${normal}"
python3 manage.py createsuperuser --username admin
