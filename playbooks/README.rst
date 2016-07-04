Ansible Playbooks
=================
Summary of the playbooks:

* **logs-ci-centos**: Wrapper used on CI jobs run on the ci.centos.org environment to upload logs to the artifact server

* **puppet-openstack-scenario001**: Runs `scenario001.pp`_ with run_tests.sh provided by puppet-openstack-integration
* **puppet-openstack-scenario002**: Runs `scenario002.pp`_ with run_tests.sh provided by puppet-openstack-integration
* **puppet-openstack-scenario003**: Runs `scenario003.pp`_ with run_tests.sh provided by puppet-openstack-integration

* **packstack-scenario001**: Runs `scenario001.sh`_ with run_tests.sh provided by Packstack
* **packstack-scenario002**: Runs `scenario002.sh`_ with run_tests.sh provided by Packstack
* **packstack-scenario003**: Runs `scenario003.sh`_ with run_tests.sh provided by Packstack

.. _scenario001.pp: https://github.com/openstack/puppet-openstack-integration/blob/master/fixtures/scenario001.pp
.. _scenario002.pp: https://github.com/openstack/puppet-openstack-integration/blob/master/fixtures/scenario002.pp
.. _scenario003.pp: https://github.com/openstack/puppet-openstack-integration/blob/master/fixtures/scenario003.pp

.. _scenario001.sh: https://github.com/openstack/packstack/blob/master/tests/scenario001.sh
.. _scenario002.sh: https://github.com/openstack/packstack/blob/master/tests/scenario002.sh
.. _scenario003.sh: https://github.com/openstack/packstack/blob/master/tests/scenario003.sh