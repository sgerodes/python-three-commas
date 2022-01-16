from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='three-commas',
    packages=['three_commas'],
    version='0.0.8',
    description='Python api wrapper for 3commas with extended functionality in the api, models, error handling',
    url='https://github.com/badass-blockchain/three_commas',
    author='Sergey Gerodes',
    author_email='sgerodes@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['some_module'],
    package_dir={'': 'src'},
    keywords=['python', '3commas', 'api', 'crypto', 'cryptocurrency', 'three commas', 'bitcoin', 'trading', 'btc', 'eth'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    install_requires=[
        'py3cw',
        'cachetools',
    ]
)
