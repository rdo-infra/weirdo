WeIRDO
======
**W**\e [ **I**\nstall | **I**\ntegrate | **I**\mprove ] **RDO**: An open
initiative to improve RDO_ with it's community for it's community.

.. _RDO: https://www.rdoproject.org/

Testing OpenStack_ is hard:

* There is *currently* almost 50 official `OpenStack projects`_
* There is over 1000 source and binary packages built and provided by the
  official RDO repositories
* These packages are bundled, integrated or provided by many different
  installers and vendors
* There are countless deployment use cases ranging from simple private clouds
  to large scale complex and highly available public clouds

Providing test coverage to make sure that each and every project and use case
works well is a hard problem to solve.

WeIRDO is an idea that is about leveraging the effort the community puts
towards their own CI initiative to improve the coverage that upstream RDO
provides.
This is about testing as many ways of installing, configuring and integrating
OpenStack as possible without re-inventing the wheel.

WeIRDO takes the gate jobs outside of the gate to test what RDO ships before
it’s packages even make it to the upstream OpenStack CI.

Let's work together to make RDO better.

.. _OpenStack: http://www.openstack.org/
.. _OpenStack projects: http://governance.openstack.org/reference/projects/index.html

Where can I find the WeIRDO CI Jobs ?
-------------------------------------
All RDO CI jobs are publicly available and the ones from WeIRDO are no
exception.

You can find the jobs on https://ci.centos.org/view/rdo/ under the label
WeIRDO.

Documentation
-------------
Documentation on what WeIRDO is, how it works and what it supports is available
on `ReadTheDocs.org`_

.. _ReadTheDocs.org: http://weirdo.readthedocs.org/en/latest/

Collaborators
=============
See the list of collaborators on GitHub_.

.. _GitHub: https://github.com/redhat-openstack/weirdo/graphs/contributors

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