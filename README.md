stackhpc.ipmi_exporter
=========

Deploys the IPMI exporter prometheus container

Requirements
------------

No requirements.

Role Variables
--------------

Please see `defaults/main.yml`

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: stackhpc.ipmi_exporter, var_name: 42 }

Testing locally
---------------

```
molecule test
```

License
-------

Apache

Author Information
------------------

Will Szumski
