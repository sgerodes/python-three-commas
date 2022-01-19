from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='three-commas',
    packages=['three_commas',
              'three_commas.api',
              'three_commas.api.ver1',
              'three_commas.api.v2',
              'three_commas.model'],
    version='0.0.16',
    description='Python api wrapper for 3commas with extended functionality in the api, models, error handling',
    url='https://github.com/badass-blockchain/python-three-commas',
    author='Sergey Gerodes',
    author_email='sgerodes@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['some_module'],
    package_dir={'': 'src'},
    keywords=['python', '3commas', 'api', 'crypto', 'cryptocurrency', 'three commas', 'bitcoin', 'trading', 'btc', 'eth'],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
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
