#!/bin/sh
mysql -u root -p$SQL_PASSWORD -e "drop database followme"
mysql -u root -p$SQL_PASSWORD -e  "create database followme"
rm followme/migrations/*_initial.py
python manage.py migrate
python manage.py makemigrations followme
python manage.py sqlmigrate followme 0001
bold=$(tput bold)
normal=$(tput sgr0)
python manage.py migrate
echo "${bold}When prompted enter email and password for the admin user${normal}"
python manage.py createsuperuser --username admin
