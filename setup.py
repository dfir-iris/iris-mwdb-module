from setuptools import setup

setup(
    name='iris-mwdb-module',
    python_requires='>=3.9',
    version='0.1.0',
    packages=['iris_mwdb_module', 'iris_mwdb_module.mwdb_handler'],
    url='https://github.com/dfir-iris/iris-mwdb-module',
    license='Apache Software License 3.0',
    author='DFIR-IRIS',
    author_email='contact@dfir-iris.org',
    description='`iris-mwdb-module` is a pipeline DFIR-IRIS module ingesting executable files (notably malware) into MWDB, the malware database developped by CERT-PL.',
    install_requires=[]
)
