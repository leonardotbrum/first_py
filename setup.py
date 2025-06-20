from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
    readme = readme_file.read()


with open(path.join(here, 'VERSION'), encoding='utf-8') as version_file:
    version = version_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]
    
with open(path.join(here, 'test_requirements.txt')) as test_requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    test_requirements = [line for line in test_requirements_file.read().splitlines()
                    if not line.startswith('#')]



setup(
    name="first_py",
    version=version,
    description="first_py",
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    package_data={
        "first_py": [
            # When adding files here, remember to update MANIFEST.in as well,
            # or else they will not be included in the distribution on PyPI!
            # 'path/to/data_file'
        ]
    },
    install_requires=requirements,
    tests_require=test_requirements,
)
