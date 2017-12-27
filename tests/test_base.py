import pytest
import tests.common as common
import nomad


@pytest.fixture
def nomad_setup():
    n = nomad.Nomad(uri=common.URI, port=common.NOMAD_PORT, verify=False, token=common.NOMAD_TOKEN)
    return n


# integration tests requires nomad Vagrant VM or Binary running
def test_base_get_connection_error():
    n = nomad.Nomad(
        uri="http://162.16.10.102", port=common.NOMAD_PORT, timeout=0.001, verify=False)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.evaluations["nope"]


def test_base_put_connection_error():
    n = nomad.Nomad(
        uri="http://162.16.10.102", port=common.NOMAD_PORT, timeout=0.001, verify=False)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.system.initiate_garbage_collection()


def test_base_delete_connection_error():
    n = nomad.Nomad(
        uri="http://162.16.10.102", port=common.NOMAD_PORT, timeout=0.001, verify=False)
    with pytest.raises(nomad.api.exceptions.BaseNomadException):
        j = n.job.deregister_job("example")
