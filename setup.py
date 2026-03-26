from setuptools import setup, find_packages


setup(
    name='copilot_security_workshop',
    version='0.1',
    packages=find_packages(),
    package_dir={'': '.'},
    include_package_data=True,
    install_requires=[
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'courseSecureCoding=copilot_security_workshop.cSecureCoding.src.appSecureCoding:create_app',
        ],
    },
)
