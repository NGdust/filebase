from setuptools import setup


setup(
    name='filebase',                    # package name
    version='0.2',                          # version
    description='Job with storage',      # short description
    url='http://index.kvando.tech',               # package URL
    install_requires=['boto3', 'google-cloud-storage'],                    # list of packages this package depends
    packages=['filebase'],              # List of module names that installing
)
