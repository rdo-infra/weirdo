How does it work ?
==================
In a nutshell
~~~~~~~~~~~~~
WeIRDO is a collection of Ansible_ roles and playbooks.

WeIRDO, through Ansible, will:

- Create an ephemeral node on which the CI job is run
- Generate a similar environment to the gate (setup configuration, packages,
  dependencies)
- Run the gate job (i.e, ``./run_tests.sh`` or ``tox`` provided by the upstream
  project)
- Destroy the ephemeral environment

Combined with Jenkins_, WeIRDO can run these tasks and report on either success
or failure.

Puppet-Openstack
~~~~~~~~~~~~~~~~
Puppet-Openstack_ gates every commit that is done with syntax, unit and
integration tests.

.. image:: images/puppet-openstack.png

These tests ensure there is no regression when someone contributes to one of
the many modules involved in Puppet-Openstack.

While the `syntax and unit`_ checks are supplied by each respective puppet
module, the integration tests are provided through the
puppet-openstack-integration_ project.
Ultimately, these are all configured to run by Jenkins through project-config_
and are triggered by Gerrit.

The integration tests are of particular interest since the puppet modules will
install OpenStack libraries, clients and services with the packages provided
through RDO_. Tempest is currently the only exception and is installed from
source.

Puppet-Openstack uses these integration tests to ensure their puppet modules
work well.

WeIRDO leverages these integration tests to ensure that the packages provided
by RDO work well.

Test implementation
-------------------
This is what the WeIRDO implementation looks like for puppet-openstack:

.. graphviz::

    digraph {
      a  [shape = polygon, sides = 4,label = <Provision test node<br/><FONT POINT-SIZE='10'><I>playbooks/roles/ci_centos/tasks/provision</I></FONT>>]
      b  [shape = polygon, sides = 4,label = <Install dependencies<br/><FONT POINT-SIZE='12'>(ruby-devel, rubygems, etc.)</FONT><br/><FONT POINT-SIZE='10'><I>playbooks/roles/puppet-openstack/tasks/packages</I></FONT>>]
      c  [shape = polygon, sides = 4,label = <Clone puppet-openstack-integration<br/><FONT POINT-SIZE='10'><I>playbooks/roles/puppet-openstack/tasks/setup</I></FONT>>]
      d  [shape = polygon, sides = 4,label = <Execute run_tests.sh<br/><FONT POINT-SIZE='12'>(with scenario001, scenario002, etc.)</FONT><br/><FONT POINT-SIZE='10'><I>playbooks/roles/puppet-openstack/tasks/run</I></FONT>>]
      e  [shape = polygon, sides = 4,label = "Install puppet, puppet modules"]
      f  [shape = polygon, sides = 4,label = "Deploy OpenStack"]
      g  [shape = polygon, sides = 4,label = "Run Tempest smoke"]
      h  [shape = polygon, sides = 4,label = <Destroy test node<br/><FONT POINT-SIZE='10'><I>playbooks/roles/ci_centos/tasks/release</I></FONT>>]

      subgraph cluster_0 {
        label = "WeIRDO";
        style = "dashed";
        a -> b -> c -> d;
      }

      subgraph cluster_1 {
        label = "puppet-openstack-integration";
        style = "dashed";
        d -> e -> f -> g;
      }

      subgraph cluster_2 {
        label = "WeIRDO";
        style = "dashed";
        g -> h;
      }
    }

Jenkins integration
-------------------
Integration in Jenkins is made with a simple Shell provisioner and it looks
like this::

    virtualenv jobenv
    source jobenv/bin/activate
    # Install WeIRDO
    pip install -e git+https://github.com/dmsimard/weirdo.git@master#egg=weirdo
    # Need features from Ansible 2 which is not yet release
    pip install -e git+https://github.com/ansible/ansible.git@v2.0.0-0.6.rc1#egg=ansible

    pushd jobenv/src/weirdo
    python setup.py install
    popd

    pushd jobenv/usr/local/share/weirdo
    mv ansible.cfg.example ansible.cfg

    ansible-playbook -vv playbooks/puppet-openstack-scenario001.yml
    result=$?

    exit $result

.. _Ansible: http://www.ansible.com/
.. _Jenkins: #jenkins-integration
.. _Puppet-Openstack: https://wiki.openstack.org/wiki/Puppet
.. _puppet-openstack-integration: https://github.com/openstack/puppet-openstack-integration
.. _syntax and unit: https://github.com/openstack/puppet-nova/blob/master/Rakefile
.. _project-config: https://github.com/openstack-infra/project-config
.. _RDO: https://www.rdoproject.org/