Jenkins job configuration
=========================
You can set up the WeIRDO jobs on any Jenkins server with the provided
`Jenkins Job Builder`_ (JJB) configuration files.

**Note**: Right now the only supported deployment target is on the bare metal
infrastructure provided by `ci.centos.org`_. As such, the jenkins slave on
which these jobs will run requires privileged network connectivity and
credentials. As new deployment targets become available, we can remove this
limitation to run these jobs truly anywhere.

.. _Jenkins Job Builder: http://ci.openstack.org/jenkins-job-builder/
.. _ci.centos.org: https://ci.centos.org/

Using Jenkins Job Builder
-------------------------
Jenkins job builder makes it easier to develop, maintain and version jobs.

To install it::

    pip install jenkins-job-builder

Create your ``config.ini`` from the ``config.ini.sample`` file, according to
your Jenkins configuration, then create/update the jobs, a bit like this::

    git clone https://github.com/redhat-openstack/weirdo.git
    cd weirdo/jenkins
    cp config.ini.sample config.ini
    # Edit config.ini to use your jenkins instance and credentials
    vi config.ini
    jenkins-jobs --conf config.ini update jobs

Jenkins plugins
---------------
There are a number of Jenkins plugins that are required or otherwise nice to
have for best results and to run these jobs with full functionality, here's a
list:

**Required**
* Python_: Required - to execute python script files
* ShiningPanda_: Required - For python helpers, virtual environment, etc.
* `GIT plugin`_: For cloning repositories and checking out revisions
* `Gerrit Trigger`_: For watching gerrit reviews patchsets and trigger gate
  jobs

**Nice to have**

* `OWASP Markup Formatter Plugin`_: For HTML markup in job descriptions
  (Enable "*Safe HTML*" Markup Formatter in Manage Jenkins -> Configure Global
  security)
* AnsiColor_: For colorized output in Jenkins console
* Timestamper_: For timestamps in Jenkins console
h
.. _Python: https://wiki.jenkins-ci.org/display/JENKINS/Python+Plugin
.. _ShiningPanda: https://wiki.jenkins-ci.org/display/JENKINS/ShiningPanda+Plugin
.. _GIT plugin: https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin
.. _Gerrit Trigger: https://wiki.jenkins-ci.org/display/JENKINS/Gerrit+Trigger
.. _OWASP Markup Formatter Plugin: https://wiki.jenkins-ci.org/display/JENKINS/OWASP+Markup+Formatter+Plugin
.. _AnsiColor: https://wiki.jenkins-ci.org/display/JENKINS/AnsiColor+Plugin
.. _Timestamper: https://wiki.jenkins-ci.org/display/JENKINS/Timestamper

Other required configuration
----------------------------
There's some required Jenkins system and plugin configuration to do which is
not provided by JJB.

Gerrit
~~~~~~
The Gerrit Trigger Plugin requires a Gerrit server to be configured in order to
allow the Jenkins instance to listen to the GerritHub event stream.

This is done in ``Manage Jenkins`` -> ``Gerrit Trigger`` ->
``Add new server``::

    name: rdo-ci-centos # This name is used in the JJB files, it's important.
    hostname: review.gerrithub.io
    frontend url: https://review.gerrithub.io/
    ssh port: 29418
    username: <your gerrithub username>
    email: <your email>
    ssh keyfile: <path to your ssh keyfile>

The remainder of the defaults should be good or up to your discretion.

SSH Key
~~~~~~~
The Git SCM plugin expects a SSH key to clone the WeIRDO repository from
GerritHub, you need to configure one.

This is done in ``Manage Jenkins`` -> ``Manage Credentials`` ->
``Add Credentials`` -> ``SSH username with private key``::

    name: rdo-ci-centos # This name is used in the JJB files, it's important.
    private key: <your private key as file, text, etc>

    ADVANCED:
    ID: aeb3af4f-6985-4c8f-8261-ec37cacad10b # This ID is used in the JJB files, it's important.

Python version
~~~~~~~~~~~~~~
The ShiningPanda plugin expects to have a Python binary called
``system-CPython-2.7``. You may need to configure it if it's not there by
default.

This is done in ``Manage Jenkins`` -> ``Configure System`` ->
``Python`` -> ``Python Installations`` -> ``Add Python``::

    name: System-CPython-2.7 # This name is used in the JJB files, it's important.
    home or executable: /usr/bin/python2.7

Jenkins slave: Label
~~~~~~~~~~~~~~~~~~~~
The jobs are set to run on any slave/node with the label ``rdo``. You need to
make sure this is configured on the nodes you want the jobs to run on.

This is done in ``Managed Jenkins`` -> ``Managed Nodes`` -> <*node*> ->
``Configure``::

    labels: rdo

Jenkins slave: CICO environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is **only** required when running jobs on the ci.centos.org
infrastructure. WeIRDO leverages python-cicoclient_ which provides an ansible
module to consume the ephemeral bare metal provisioning infrastructure.

You need to set your ci.centos.org API key as well as the path to the SSH key
used when connecting to the nodes as environment variables on your slave
node(s).

This is done in ``Managed Jenkins`` -> ``Managed Nodes`` -> <*node*> ->
``Configure`` -> ``Node properties`` -> ``Environment variables`` -> ``Add``::

    name: CICO_API_KEY
    value: <api key>

    name: CICO_SSH_KEY
    value: <path to private key>

.. _python-cicoclient: http://python-cicoclient.readthedocs.org/en/latest/