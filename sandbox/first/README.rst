The First Django App
====================

Based on the tutorial in Django documentation.

Basic Things
------------

There are basic scripts and files you need to start a simple Django
application.
Buildout will make things a lot easier and save a lot time.
Here, the only requirment is you have Python installed.
We will start from Python version 3.x.

django-admin
~~~~~~~~~~~~

Buildout will be used for the whole playing experience.

using the following part to generate django-admin script.::

  [django-admin]
  recipe = zc.recipe.egg
  eggs = ${buildout:eggs}
  entry-points = django-admin=django.core.management:execute_from_command_line

start a project
~~~~~~~~~~~~~~~

create a project using the Django admin script.::

  $ buildout/bin/django-admin startproject leocornus_django_sandbox_first sandbox/first

generate the manage script for first project.::

  [first-manage]
  recipe = zc.recipe.egg
  eggs = ${buildout:eggs}
  entry-points = first-manage=django.core.management:execute_from_command_line
  extra-paths = 
      ${buildout:directory}/../sandbox/first

Runserver
~~~~~~~~~

To runserver, we need setup the environment variable
**DJANGO_SETTINGS_MODULE**.
Here are the steps::

  $ export DJANGO_SETTINGS_MODULE=leocornus_django_sandbox_first.settings
  $ buildout/bin/first-manage runserver

migrate
~~~~~~~

Why we need execute migrate command?::

  $ bin/first-manage migrate

Test Driving
------------
