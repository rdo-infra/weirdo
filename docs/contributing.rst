Contributing
============
WeIRDO was built from the ground up with the highest standards and best
practices in mind just like OpenStack.

To try and keep it that way, commits to WeIRDO are first reviewed through
Gerrit and are gated against jobs to ensure the patch does not break anything.

Gate jobs
---------
* **weirdo-gate-tox-ansible-lint** checks that playbooks, roles and tasks are
  clean and "compile"
* **weirdo-gate-tox-jjb** checks that the JJB configuration files "compile"
* **weirdo-gate-tox-docs** checks that documentation can be built properly

* **weirdo-gate-ansible-\*** runs the integration tests implemented in WeIRDO

Getting started
---------------
The process is very similar to what someone would expect when contributing to
an OpenStack project except WeIRDO leverages the gerrit instance at
`gerrithub.io`_.

You can submit a patch to WeIRDO by doing something like this::

    # git-review is required and can be installed through pip
    pip install git-review
    git clone https://github.com/redhat-openstack/weirdo.git
    cd weirdo
    # < Some hacking occurs >
    git commit -a -m "Fixing things"
    git review

.. _gerrithub.io: https://review.gerrithub.io/#/q/project:redhat-openstack/weirdo
