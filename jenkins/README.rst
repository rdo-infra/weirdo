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
Jenkins job builder makes it easier to maintain and version Jenkins job.

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

* ShiningPanda_: Required - For python helpers, virtual environment, etc.
* `GIT plugin`_: For cloning repositories and checking out revisions
* `Gerrit Trigger`_: For watching gerrit reviews patchsets and trigger gate
  jobs

**Nice to have**

* `OWASP Markup Formatter Plugin`_: For HTML markup in job descriptions
  (Enable "*Safe HTML*" Markup Formatter in Manage Jenkins -> Configure Global
  security)
* AnsiColor_: For colorized output in Jenkins console
* Timestamper_: For timestamps in Jenkins console

Other required configuration
----------------------------
There's some jenkins configuration to do as well which is not provided by JJB.

Gerrit
~~~~~~
You need to configure the Gerrit Trigger plugin and add the GerritHub instance
so Jenkins can use it.

This is done in ``Manage Jenkins`` -> ``Gerrit Trigger``::

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
You need to configure a ssh key to be used by the Git SCM plugin so it can
clone the repository from GerritHub.

This is done in ``Manage Jenkins`` -> ``Manage Credentials`` ->
``Add Credentials`` -> ``SSH username with private key``::

    name: rdo-ci-hudson # This name is what is used in the JJB files, it's important.
    private key: <your private key as file, text, etc>

    ADVANCED:
    ID: aeb3af4f-6985-4c8f-8261-ec37cacad10b # This ID is used in the JJB files, it's important

.. _ShiningPanda: https://wiki.jenkins-ci.org/display/JENKINS/ShiningPanda+Plugin
.. _GIT plugin: https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin
.. _Gerrit Trigger: https://wiki.jenkins-ci.org/display/JENKINS/Gerrit+Trigger
.. _OWASP Markup Formatter Plugin: https://wiki.jenkins-ci.org/display/JENKINS/OWASP+Markup+Formatter+Plugin
.. _AnsiColor: https://wiki.jenkins-ci.org/display/JENKINS/AnsiColor+Plugin
.. _Timestamper: https://wiki.jenkins-ci.org/display/JENKINS/Timestamper
