#  MHAN-team Service

## Description

MAHN-team web site hosts the FollowMe application.

## Requirements

* python 3.5.1
* django 1.9.3
* mysql 5.7.12

## Development Tools

* Pycharm Community Edition
* SourceTree
* sqlworkbench 1.10.2

## How to run the server

```
> git clone https://github.com/mhan-team/service.git
> cd service/mhan-service
> python manage.py runserver <IP address>:8000
```

Point your web browser to http://<IP address>:8000

## To run the FollowMe application

Point your web browser to http://<IP address>:8000/followme

## To run the Administration web application

Point your web browser to http://<IP address>:8000/admin

## Initial database setup

You perform this step only the first time you run the server on your machine.

* Install mysql server and client
* Set root password and create followme database

    ```
    > mysql
    mysql> SET PASSWORD FOR 'root'@'localhost' = PASSWORD('!topsecret');
    mysql> mysql -u root -p
    mysql> create database followme;
    ```
* Get django to create the database tables.  From the mhan_service directory,

```
> python manage.py migrate
```

## Database migration after initial setup or after a change to the models

To generate a migration file:

```
> python manage.py makemigrations followme
```

To generate the SQL script for the migration:

```
> python manage.py sqlmigrate followme 0001
```
To execute generated SQL script against an existing database:

```
> python manage.py migrate
```

## Re-initialize the database when it already exists

```
mysql> drop database followme;
mysql> create database followme;
```

Then continue with database migration described in previous section