Changelog:
--------

`2.1.0rc1`:

* buffer for pdf is no longer a string

`2.0.6`:

* python 3.9 is now supported
* change Pillow dependency version for python 3.9 compatibility

`2.0.5`:

* fix image `x` offset -`cgfrost`
* add exceptions (`class FPDFException(Exception)` and
  `class FPDFPageFormatException(FPDFException)`)
* add tests to increase line coverage in `image_parsing` module
* add a test which uses most of the HTML features
* improve code quality and readability for font handling (weight and style) -`cgfrost`

`2.0.4`:

* add missing import statment for `urlopen` in `image_parsing` module
* change urlopen import from `six` library to maintain python2 compatibility
* change `load_resource` function to understand a bytesio argument, dont re-read
  the image if `isinstance(filename, BytesIO)`.

`2.0.3`:

 * Change to `setup(packages = find_packages())`

`2.0.2`:

 * Attempt to fix missing `fpdf.util`, delete from [PyPI.org][2]

`2.0.1`:

 * Clean up links and text files
 * Start to refactor syntax into own functions for readability
 * Replace pixel regexes with numpy in image parsing (s/o @pennersr)

[2]: https://pypi.org/project/fpdf2/2.0.2/
