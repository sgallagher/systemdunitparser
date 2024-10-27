from setuptools import setup

with open("README.md") as i:
    _long_description = i.read()

setup(
    name='systemdunitparser',
    author_email='sgallagh@redhat.com',
    author='Stephen Gallagher',
    description='Parser to read and create unit files for systemd',
    license='GPL-3.0-or-later',
    long_description=_long_description,
    long_description_content_type="text/markdown",
    packages=['SystemdUnitParser'],
    url='http://github.com/sgallagh/systemdunitparser',
    version='0.3',
    license_files=('LICENSE',),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
