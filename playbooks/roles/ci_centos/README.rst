ci_centos
=========
This role wraps around the Ansible module provided by python-cicoclient_ to
request and release bare metal servers from the `ci.centos.org`_ environment.

.. _python-cicoclient: https://github.com/dmsimard/python-cicoclient
.. _ci.centos.org: https://ci.centos.org/

Included tasks
~~~~~~~~~~~~~~

* ``provision``: Requests a node of the provided specifications
* ``release``: Release the nodes tied to the current session
