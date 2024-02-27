Victoriametrics Single
=========

This role will install and configure a single instance of VictoriaMetrics.

Requirements
------------

You need to enable the gathering of facts in your playbook.

Role Variables
--------------

Variable can be found in `defaults/main.yml` and are as follows: [Click here](defaults/main.yml)


Dependencies
------------

This role does not have any dependencies.

Example Playbook
----------------

    - hosts: victoriametrics-single
      roles:
         - { role: msterhuj.victoriametrics_single }

License
-------

GNU GPLv3

Author Information
------------------

msterhuj
