from setuptools import setup, find_packages
import gdoc_down
import os

# parse requirements.txt
install_requires = [line.rstrip() for line in open('requirements.txt')]

setup(
    name="gdoc-down",
    version=gdoc_down.__version__,
    description="Download Google documents to files",
    url="https://github.com/KarrLab/gdoc-down",
    download_url='https://github.com/KarrLab/gdoc-down/tarball/{}'.format(gdoc_down.__version__),
    author="Jonathan Karr",
    author_email="jonrkarr@gmail.com",
    license="MIT",
    keywords='Google documents drive download latex tex html pdf docx',
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={
        'gdoc_down': ['client.json'],
    },
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Communications :: File Sharing',
        'Topic :: Office/Business :: Office Suites',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': [
            'gdoc-down = gdoc_down.__main__:main',
        ],
    },
)