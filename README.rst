=================
services-registry
=================

|python| |version|

.. |version| image:: http://img.shields.io/pypi/v/services-registry.svg
  :target: https://pypi.python.org/pypi/services-registry

.. |python| image:: https://img.shields.io/pypi/pyversions/services-registry.svg
  :target: https://pypi.python.org/pypi/services-registry/

A registry to manage services in a Python application.

Description
===========

* Registry keeps track of all initialized services and returns corresponding services handlers to caller.
* Registry initializes a service if it has not been initialized before being requested.
* Registry makes sure that at any point of time, at most one service registry handler exists.

Usage
=====

1. Services must inherit from the ``services_registry.services_registry.Service`` class. For example:

.. code-block::

    from services_registry.services_registry import Service


    class MyService(Service):
        pass


2. Services registry can be used in code in thr following way:

.. code-block::

    from services_registry.services_registry import services_registry


    my_service = services_registry.get_service(MyService)

License
=======

Distributed under the terms of the `MIT`_ license.

.. _MIT: https://github.com/ygrebnov/services-registry/blob/master/LICENSE