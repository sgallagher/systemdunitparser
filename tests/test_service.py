import os

from SystemdUnitParser import SystemdUnitParser

TESTDIR = os.path.abspath(os.path.dirname(__file__))


class TestMopidyService:

    def test_unit_section(self):
        config = SystemdUnitParser()
        config.read(os.path.join(TESTDIR, 'mopidy.service'))

        # Verify Description
        assert config['Unit']['Description'] == 'Mopidy music server'

        # Verify After (multiple values become a tuple, check by inclusion)
        after_values = config['Unit']['After']
        assert isinstance(after_values, tuple)
        assert len(after_values) == 7
        assert 'avahi-daemon.service' in after_values
        assert 'dbus.service' in after_values
        assert 'network-online.target' in after_values
        assert 'nss-lookup.target' in after_values
        assert 'pulseaudio.service' in after_values
        assert 'remote-fs.target' in after_values
        assert 'sound.target' in after_values

        # Verify Wants
        assert config['Unit']['Wants'] == 'network-online.target'

    def test_service_section(self):
        config = SystemdUnitParser()
        config.read(os.path.join(TESTDIR, 'mopidy.service'))

        # Verify ExecStart
        assert config['Service']['ExecStart'] == '/usr/bin/mopidy'

        # Verify Environment (multiple values become a tuple, check by inclusion)
        env_values = config['Service']['Environment']
        assert isinstance(env_values, tuple)
        assert len(env_values) == 2
        assert '"GST_DEBUG=librespot:6,spotifyaudiosrc:4"' in env_values
        assert '"GST_DEBUG_LIBRESPOT=DEBUG"' in env_values

    def test_install_section(self):
        config = SystemdUnitParser()
        config.read(os.path.join(TESTDIR, 'mopidy.service'))

        # Verify WantedBy
        assert config['Install']['WantedBy'] == 'default.target'

    def test_all_sections_present(self):
        config = SystemdUnitParser()
        config.read(os.path.join(TESTDIR, 'mopidy.service'))

        assert 'Unit' in config.sections()
        assert 'Service' in config.sections()
        assert 'Install' in config.sections()
        assert len(config.sections()) == 3

