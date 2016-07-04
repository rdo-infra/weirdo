Using WeIRDO with Jenkins
=========================
There are currently two different implementations of WeIRDO jobs that are run
through Jenkins.

* Periodic jobs in a pipeline for trunk package testing and promotion on `ci.centos.org`_
* Gate jobs against WeIRDO itself as well as against other projects on `review.rdoproject.org`_

.. _ci.centos.org: https://ci.centos.org
.. _review.rdoproject.org: https://review.rdoproject.org

ci.centos.org: Pure jenkins and JJB on external bare metal
----------------------------------------------------------
The configuration for the jobs that leverage WeIRDO on ci.centos.org to test
RDO trunk repositories can be found in the `rdo-infra/ci-config`_ repository.

The WeIRDO jobs themselves and their results are publicly available on
https://ci.centos.org/view/rdo/view/promotion-pipeline/

ci.centos.org provides an API, called Duffy_, to manage ephemeral bare metal
nodes to run jobs on. As such, the jobs that run on this environment have
particular requirements and are documented in the `rdo-infra/ci-config`_
repository.

In this use case, a task is executed before WeIRDO runs to request a bare metal
node and an inventory is created with that node in it. After that, WeIRDO runs
with the generated inventory file, logs are collected and uploaded to
`ci.centos.org/artifacts`_ and the node is destroyed.

.. _rdo-infra/ci-config: https://github.com/rdo-infra/ci-config
.. _Duffy: https://wiki.centos.org/QaWiki/CI/Duffy
.. _ci.centos.org/artifacts: https://ci.centos.org/artifacts/rdo/

Troubleshooting ci.centos.org jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A logs.html file will be saved as an artifact of the job. This logs.html file
is actually just a redirection to the location where the logs are located for
this particular job.

review.rdoproject.org: JJB with Gerrit, Zuul and Nodepool virtual machines
--------------------------------------------------------------------------
review.rdoproject.org is an environment driven by Gerrit, Zuul and Jenkins and
jobs run on ephemeral jenkins slaves provided by Nodepool, it is a
`software factory`_ instance that attempts to provide the same experience as
the one provided by openstack-infra_ for their continuous integration ecosystem.

The configuration for the different components can be found in the config_
repository.

In this use case, nodepool takes care of the node provisioning and destruction
before and after the job and the jenkins slave is effectively "localhost".
To run WeIRDO on localhost, we create a minimal inventory file with localhost
as the target and pre-install some dependencies beforehand. Once the job is
over, artifacts and logs are uploaded to Swift.

.. _software factory: http://softwarefactory-project.io/docs/intro.html
.. _openstack-infra: http://docs.openstack.org/infra/system-config/
.. _config: https://review.rdoproject.org/r/gitweb?p=config.git;a=summary

Troubleshooting review.rdoproject.org jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WeIRDO runs from gate jobs in review.rdoproject.org's Gerrit. Clicking on a
Job in a Jenkins comment in a review will lead you to the Jenkins job result
and console.
To access the job logs, click on the console log and the link to the logs will
be available at the very bottom of the log, provided by zuul-swift-uploader.