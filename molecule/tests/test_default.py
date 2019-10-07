import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    dirs = [
        "/etc/ipmi-exporter"
    ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists


def test_files(host):
    files = [
        "/etc/ipmi-exporter/ipmi.yml",
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_socket(host):
    sockets = [
        "tcp://127.0.0.1:9290"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
