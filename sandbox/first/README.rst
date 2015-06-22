The First Django Project 
========================

Based on the tutorial in Django documentation.

django-admin
------------

There are basic scripts and files you need to start a simple Django
application.
Buildout will make things a lot easier and save a lot time.
Here, the only requirment is you have Python installed.
We will start from Python version 3.x.

Buildout will be used for the whole playing experience.

using the following part to generate **django-admin** script.::

  [django-admin]
  recipe = zc.recipe.egg
  eggs = ${buildout:eggs}
  entry-points = django-admin=django.core.management:execute_from_command_line

start a project
---------------

A Django project is like a hosting place for hosting Django apps.
A projct will have the following basic files::

  [PROJECT NAME]
    |- __init__.py
    |- settings.py
    |- urls.py
    |- wsgi.py

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

  $ buildout/bin/first-manage migrate

Test Driving
------------

Mainly try to anwser the following questions:

- how to prepare testcases?
- how to run testcase?
- how to manage and mock the dependences for testcases?

preparing test cases
~~~~~~~~~~~~~~~~~~~~

Django has a TestCase class in module **django.test**.
The simple way to create a test case is extending this class.
A simple test case clould as simple as this::

  from django.test import TestCase

  class BasicTestCase(TestCase):
      """a simple test case"""

      def setUp(self):
          """Empty for now."""

      def test_assert(self):
          """testing assert functions"""
          self.assertEqual('abc', 'abc')

run test cases
~~~~~~~~~~~~~~

How to run test cases depends on how the test cases are organized.
In this case here, we storied the test cases like following::

  leocornus_django_sandbox_first/
    |- test/
        |- testBasic.py

Then, we could run test cases using this command::

  $ buildout/bin/first-manage test leocornus_django_sandbox_first.test

moch and testing db
~~~~~~~~~~~~~~~~~~~

Start first app
---------------

Django admin script has a task to create Django app.::

  $ buildout/bin/django-admin startapp polls sandbox/first/.../polls

It will create the skeleton for a Django app.
