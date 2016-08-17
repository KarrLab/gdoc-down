[![PyPI package](https://img.shields.io/pypi/v/gdoc-down.svg)](https://pypi.python.org/pypi/gdoc-down)
[![Documentation](https://readthedocs.org/projects/gdoc-down/badge/?version=latest)](http://gdoc-down.readthedocs.org)
[![Test results](https://circleci.com/gh/KarrLab/gdoc-down.svg?style=shield)](https://circleci.com/gh/KarrLab/gdoc-down)
[![Test coverage](https://coveralls.io/repos/github/KarrLab/gdoc-down/badge.svg)](https://coveralls.io/github/KarrLab/gdoc-down)
[![Code analysis](https://codeclimate.com/github/KarrLab/gdoc-down/badges/gpa.svg)](https://codeclimate.com/github/KarrLab/gdoc-down)
[![License](https://img.shields.io/github/license/KarrLab/gdoc-down.svg)](LICENSE)

# `gdoc-down`
API and command line program to save Google documents to local files in several formats:
* HTML (.html)
* LaTeX (.tex)
* Open document format (.odt)
* Plain text (.txt)
* Portable document format (.pdf)
* Rich text format (.rtf)
* Word documents (.docx)

The software has several special features for handling LaTeX files:
* The program ignores all images. This allows the user to place images inside the Google 
  document for convenience and to use \includegraphics to embed images in compile PDF files.
* The program will convert all Google document comments to PDF comments.
* The program ignores all page breaks.

The first time the program is called, the program will request access to the user's Google
account. This will create a client.json file in the users home directory (~/.gdoc-down/client.json).

## Installation
```
pip install gdoc-down
```

## Command line usage
```
usage: gdoc-down (sub-commands ...) [options ...] {arguments ...}

Download Google documents to local files in various formats

positional arguments:
  gdoc_file             path to Google document

optional arguments:
  -h, --help            show this help message and exit
  --debug               toggle debug output
  --quiet               suppress all output
  --format FORMAT, -f FORMAT
                        output format (docx, html, odft, pdf, rtf, tex, txt)
  --out_path OUT_PATH, -o OUT_PATH
                        path where Google document should be downloaded
  --extension EXTENSION, -e EXTENSION
                        output extension
```

## Documentation
Please see the documentation at [Read the Docs](http://gdoc-down.readthedocs.io).

## Tests
`nose` can be used to run the tests:
```
nosetests tests
```

Please note that several additional packages are required for testing (see [tests/requirements.txt](tests/requirements.txt)).

## License
The example model is released under the [MIT license](LICENSE).

## Development team
`gdoc-down` was developed by [Jonathan Karr](http://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York, USA.

## Questions and comments
Please contact the [Jonathan Karr](http://www.karrlab.org) with any questions or comments.
