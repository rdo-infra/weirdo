Contributing
============
WeIRDO was built from the ground up with the highest standards and best
practices in mind just like OpenStack.

To try and keep it that way, commits to WeIRDO are first reviewed through
Gerrit and are gated against jobs to ensure the patch does not break anything.

Gate jobs
---------
* **gate-weirdo-ansible-lint** checks that playbooks, roles and tasks are
  clean and "compile"
* **gate-weirdo-docs** checks that documentation can be built properly

* **gate-weirdo-integration-\*** runs the integration tests implemented in
  WeIRDO whenever relevant (i.e, only run Packstack integration tests when
  commits involve code that touches Packstack)

Getting started
---------------
The process is very similar to what someone would expect when contributing to
an OpenStack project except WeIRDO leverages the gerrit instance at
`review.rdoproject.org`_.

You can submit a patch to WeIRDO by doing something like this::

    # git-review is required and can be installed through pip
    pip install git-review
    git clone https://github.com/rdo-infra/weirdo.git
    cd weirdo
    # < Some hacking occurs >
    git commit -a -m "Fixing things"
    git review

.. _review.rdoproject.org: https://review.rdoproject.org
