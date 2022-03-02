import os

import pytest
from SystemdUnitParser import SystemdUnitParser

TESTDIR = os.path.abspath(os.path.dirname(__file__))


class TestBasic():

    def test_parsing(self):
        config = SystemdUnitParser()
        config.read(os.path.join(TESTDIR, 'sample.service'))
        assert config['Service']['ExecStartPre'] == (
            '/bin/sh -c "foo && bar && baz"', '/bin/sh -c "magic"')
        assert config['Service']['ExecStart'] == '/usr/bin/application'
