puppet-openstack
----------------
This role provides an implementation of the
puppet-openstack-integration_ gate jobs.

.. _puppet-openstack-integration: https://github.com/openstack/puppet-openstack-integration

Supported gate jobs
~~~~~~~~~~~~~~~~~~~

* gate-puppet-openstack-integration-scenario001-dsvm-centos7
* gate-puppet-openstack-integration-scenario002-dsvm-centos7

Included tasks
~~~~~~~~~~~~~~

* ``packages``: Ensures required dependencies are installed
* ``setup``: Clones the repository
* ``run``: Runs the integration tests
