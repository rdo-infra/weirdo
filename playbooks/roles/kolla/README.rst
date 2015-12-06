kolla
-----
This role provides an implementation of the Kolla_ gate jobs.

.. _Kolla: https://github.com/openstack/kolla

Supported gate jobs
~~~~~~~~~~~~~~~~~~~

* gate-kolla-dsvm-build-centos-binary
* gate-kolla-dsvm-deploy-centos-binary

Included tasks
~~~~~~~~~~~~~~

* ``packages``: Ensures required dependencies are installed
* ``setup``: Configures a block device for usage with Docker, clones the
  repository and installs the requirements.
* ``run``: Runs the integration tests
