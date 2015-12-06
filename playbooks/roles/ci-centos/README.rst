ci-centos
---------
This role wraps around the Ansible module provided by python-cicoclient_ to
request and release bare metal servers from the `ci.centos.org`_ environment.

.. _python-cicoclient: https://github.com/dmsimard/python-cicoclient
.. _ci.centos.org: https://ci.centos.org/

Requirements
~~~~~~~~~~~~
The python-cicoclient ansible module requires two environment variable to be
set::

    CICO_API_KEY: Your ci.centos.org API key
    CICO_SSH_KEY: Path to the ssh key to log on to the CI nodes

Included tasks
~~~~~~~~~~~~~~

* ``provision``: Requests a node of the provided specifications
* ``release``: Release the nodes tied to the current session
