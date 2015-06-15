__author__ = 'sgallagh'

from SystemdUnitParser import SystemdUnitParser

config = SystemdUnitParser()

config.read('/etc/systemd/system/parsertest.service')

print(config['Service']['ExecStartPre'])
print(config['Service']['ExecStart'])