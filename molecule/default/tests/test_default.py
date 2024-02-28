def test_account_present(host):
    group = host.group("victoriametrics")
    user = host.user("victoriametrics")
    assert group.exists
    assert user.exists

def test_directory(host):
    # check owner and permission 0755
    dirs = [
        "/var/lib/victoriametrics",
        "/etc/victoriametrics",
    ]

    for folder in dirs:
        d = host.file(folder)
        assert d.is_directory
        assert d.user == "victoriametrics"
        assert d.group == "victoriametrics"
        assert oct(d.mode) == "0o755"

def test_config_file(host):
    config = host.file("/etc/victoriametrics/promscrape.yml")
    assert config.exists
    assert config.user == "victoriametrics"
    assert config.group == "victoriametrics"
    assert oct(config.mode) == "0o644"

def test_binary(host):
    binary = host.file("/usr/local/bin/victoria-metrics-prod")
    assert binary.exists
    assert oct(binary.mode) == "0o755"

def test_service_file(host):
    service_file = host.file("/etc/systemd/system/victoriametrics.service")
    assert service_file.exists

def test_service(host):
    service = host.service("victoriametrics")
    assert service.is_enabled
    assert service.is_running

def test_socket(host):
    socket = host.socket("tcp://0.0.0.0:8428")
    assert socket.is_listening

def test_cleanup(host):
    files = [
        "/tmp/victoria-metrics-prod"
        "/tmp/victoria-metrics.tar.gz"
    ]
    
    for file in files:
        f = host.file(file)
        assert not f.exists