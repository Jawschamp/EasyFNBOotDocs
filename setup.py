import setuptools
import re

long_description = ''


version = ''


requirements = ['aiohttp>=3.3', 'aioxmpp>=0.10.4']
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    pass

extras_require = {
    'docs': [
        'sphinxcontrib_trio==1.1.0',
    ]
}

setuptools.setup(
    name="fortnitepy",
    url="https://github.com/Terbau/fortnitepy",
    project_urls={
        "Documentation": "https://fortnitepy.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/Terbau/fortnitepy/issues",
    },
    version=version,
    author="Terbau",
    description="Library for interacting with fortnite services",
    long_description=long_description,
    license='MIT',
    long_description_content_type="text/markdown",
    install_requires=requirements,
    extras_require=extras_require,
    packages=setuptools.find_packages(),
    python_requires='>=3.5.3',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
