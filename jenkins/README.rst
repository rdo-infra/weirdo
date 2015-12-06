These are Jenkins job builder configuration files for use with WeIRDO.

You can replicate the jobs by installing Jenkins Job Builder (JJB)::

    pip install jenkins-job-builder

Create your config.ini from the config.ini.sample file, according to your
Jenkins configuration, then create/update the jobs, a bit like this::

    git clone https://github.com/redhat-openstack/weirdo.git
    cd weirdo/jenkins
    cp config.ini.sample config.ini
    # Edit config.ini to use your jenkins instance and credentials
    vi config.ini
    jenkins-jobs --conf config.ini update jobs

Further information about how to alter these files can be found in the JJB
documentation_.

Note: There are a number of Jenkins plugins required or otherwise nice to have
for best results to run these jobs with full functionality, here's a list:

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

.. _documentation: http://ci.openstack.org/jenkins-job-builder/
.. _ShiningPanda: https://wiki.jenkins-ci.org/display/JENKINS/ShiningPanda+Plugin
.. _GIT plugin: https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin
.. _Gerrit Trigger: https://wiki.jenkins-ci.org/display/JENKINS/Gerrit+Trigger
.. _OWASP Markup Formatter Plugin: https://wiki.jenkins-ci.org/display/JENKINS/OWASP+Markup+Formatter+Plugin
.. _AnsiColor: https://wiki.jenkins-ci.org/display/JENKINS/AnsiColor+Plugin
.. _Timestamper: https://wiki.jenkins-ci.org/display/JENKINS/Timestamper
