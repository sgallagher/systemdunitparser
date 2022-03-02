# SystemdUnitParser

SystemdUnitParser is an extension to Python's `configparser.RawConfigParser` to properly parse
systemd unit files

## Usage

```python
from SystemdUnitParser import SystemdUnitParser

config = SystemdUnitParser()
config.read('sample.service') # or any other systemd unit file

print(config.sections()) # get all sections of the unit file
print(config.options('Unit')) # get all options in a section
print(config.get('Unit', 'Description')) # get the actual value of an action
```

## Contributing

- create a fork
- create a new branch from origin/master
- do your patches
- run `pytest`
- push your changes to your fork and create a PR

## License

This module is licensed under `GPL-3.0-or-later`
