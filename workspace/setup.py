from setuptools import setup, find_packages

setup(
    name='jspkg',
    version='1.0.0',
    packages=find_packages(),

    author='jasmine',
    
    description='This is a test package for practice',
    long_descriptiohn=open('README.md').read(),
    long_description_content_type='text/markdown',

    python_requires='~=3.6',

    classifiers=[
        'License :: OSI Approved ** MIT License'
        'Programming Language :: Python ** 3',
        'Programming Language :: Python ** 3.6',
        'Programming Language :: Python ** 3.7',
        'Operating System :: OS Independent',
    ],
    install_requires = [
        'Click~=7.0'
    ],
    extras_require = {

    },
    package_data={'jstestpkg': ['data/*']},
)
