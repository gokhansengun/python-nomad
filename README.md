# python-nomad


Branch | Status | Coverage |
---| ---| ---
develop | [![Build Status](https://travis-ci.org/jrxFive/python-nomad.svg?branch=develop)](https://travis-ci.org/jrxFive/python-nomad) | [![codecov](https://codecov.io/gh/jrxFive/python-nomad/branch/develop/graph/badge.svg)](https://codecov.io/gh/jrxFive/python-nomad)


## Installation
```
pip install python-nomad
```

## Examples
```python


import nomad
# For HTTP Nomad instances
n = nomad.Nomad(host="172.16.100.10", timeout=5)

# For HTTPS Nomad instances with non-self-signed SSL certificates
n = nomad.Nomad(host="172.16.100.10", secured=True, timeout=5, verify=True)

# For HTTPS Nomad instances with self-signed SSL certificates and no validate the cert
n = nomad.Nomad(host="172.16.100.10", secured=True, timeout=5, verify=False)

# For HTTPS Nomad instances with self-signed SSL certificates that mus validate with cert
n = nomad.Nomad(host="172.16.100.10", secured=True, timeout=5, verify=True, cert="/path/to/certfile") # See http://docs.python-requests.org/en/master/user/advanced/#ssl-cert-verification

# For HTTPS Nomad instances with cert file and key
n = nomad.Nomad(host="https://172.16.100.10", secured=True, timeout=5, verify=True, cert=("/path/to/certfile", "/path/to/key") # See http://docs.python-requests.org/en/master/user/advanced/#ssl-cert-verification

# For HTTPS Nomad instances with namespace and acl token
n = nomad.Nomad(host="172.16.100.10", secured=True timeout=5, verify=False, namespace='Namespace-example',token='3f4a0fcd-7c42-773c-25db-2d31ba0c05fe')

"example" in n.jobs

j = n.jobs["example"]["ID"]

example_allocation = n.job.get_allocations(j)

n.job.deregister_job(j)
```

## Class Dunders
| Class | contains | len | getitem | iter |
|---|---|---|---|---|
|agent|N|N|N|N
|allocation|Y|N|Y|N
|allocations|N|Y|N|Y
|client|N|N|N|N
|evaluation|Y|N|Y|N
|evaluations|Y|Y|Y|Y
|job|Y|N|Y|N
|jobs|Y|Y|Y|Y
|node|Y|N|Y|N
|nodes|Y|Y|Y|Y
|regions|Y|Y|Y|Y
|status.leader|Y|Y|N|N
|status.peers|Y|Y|Y|Y
|system|N|N|N|N
|validate|N|N|N|N
|deployments|Y|Y|Y|Y
|deployment|Y|N|Y|N
|namespace|Y|N|Y|N
|namespaces|Y|Y|Y|Y
|acl|Y|N|Y|N
|sentinel|Y|N|Y|N

## Development
* create virtualenv and activate
* install requirements-dev.txt
* can either use the Vagrantfile for local integration testing or create environment variables `NOMAD_IP` and `NOMAD_PORT` that are assigned to a nomad binary that is running

```
virutalenv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

## Testing with vagrant and virtualbox
```
vagrant up --provider virtualbox
py.test --cov=nomad --cov-report=term-missing --runxfail tests/
```

- Examples
    - [x] Acl [:link:](docs/api/acl.md)
    - [x] Agent [:link:](docs/api/agent.md)
    - [x] Allocation [:link:](docs/api/allocation.md)
    - [x] Allocations [:link:](docs/api/allocations.md)
    - [x] Client [:link:](docs/api/client.md)
    - [x] Evaluation [:link:](docs/api/evaluation.md)
    - [x] Evaluations [:link:](docs/api/evaluations.md)
    - [x] Job [:link:](docs/api/job.md)
    - [x] Jobs [:link:](docs/api/jobs.md)
    - [x] Namespace [:link:](docs/api/namespace.md)
    - [x] Namespaces [:link:](docs/api/namespaces.md)
    - [x] Node [:link:](docs/api/node.md)
    - [x] Nodes [:link:](docs/api/nodes.md)
    - [x] Regions [:link:](docs/api/regions.md)
    - [x] Sentinel [:link:](docs/api/sentinel.md)
    - [x] Status [:link:](docs/api/status.md)
    - [x] System [:link:](docs/api/system.md)
    - [x] Validate [:link:](docs/api/validate.md)

## TODO
- [ ] functional tests
- [ ] Inherit Base class, remove duplication and override parent dunders
- [ ] readthedocs
