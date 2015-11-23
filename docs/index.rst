Welcome to the WeIRDO's documentation!
======================================
We Integrate RDO_: An open initiative to improve RDO with the help of the
community.

.. _RDO: https://www.rdoproject.org/

About this project
------------------
Testing OpenStack_ installations is complex:

* There is almost 50 official `OpenStack projects`_
* There is over 1000 source and binary packages provided by the official RDO
  repositories
* There are countless deployment use cases from simple private clouds to large
  scale complex and highly available public clouds

Providing test coverage to make sure that each and every project and use case
works well is a hard problem to solve.

WeIRDO is an attempt to leverage the effort the community puts towards their
own CI initiative to improve the coverage that upstream RDO provides.

We're taking your jobs outside the gate to test what we ship before our
packages even make it to your CI.

Let's work together to make RDO better.

.. _OpenStack: http://www.openstack.org/
.. _OpenStack projects: http://governance.openstack.org/reference/projects/index.html

Supported CI jobs
-----------------
WeIRDO currently provides an implementation for the following gate jobs:

Puppet-OpenStack
~~~~~~~~~~~~~~~~
About Puppet-OpenStack_::

    The Puppet modules for OpenStack bring scalable and reliable IT automation
    to OpenStack cloud deployments.

Supported Puppet-OpenStack gate jobs:

* gate-puppet-openstack-integration-scenario001-dsvm-centos7
* gate-puppet-openstack-integration-scenario002-dsvm-centos7

.. _Puppet-OpenStack: https://wiki.openstack.org/wiki/Puppet

Kolla
~~~~~
About Kolla_::

    Kolla provides production-ready containers and deployment tools for
    operating OpenStack clouds.

Supported Kolla gate jobs:

* gate-kolla-dsvm-build-centos-binary
* gate-kolla-dsvm-deploy-centos-binary

.. _Kolla: https://github.com/openstack/kolla

Author
======
David Moreau Simard

Copyright
=========
Copyright 2015 Red Hat, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

