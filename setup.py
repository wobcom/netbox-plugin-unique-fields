from setuptools import find_packages, setup

setup(
    name='netbox-plugin-unique-fields',
    version='0.1.0',
    description='Plugin for unique "custom" fields in Netbox v2.11.x',
    url='',
    author='Johann Wagner <johann.wagner@wobcom.de>',
    license='GPL-3.0',
    packages=find_packages(),
    include_package_data=True,
)
