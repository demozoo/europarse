europarse - dateutil.parser, but not broken
===========================================

Since version 2.5.2, the [python-dateutil](https://pypi.org/project/python-dateutil/)'s `parser` module has had [a rather severe bug](https://github.com/dateutil/dateutil/issues/402) (for non-Americans): if you specify the `dayfirst=True` option to indicate that ambiguous xx/xx/xxxx dates should be interpreted as dd/mm/yyyy, it is no longer able to parse ISO 8601 YYYY-MM-DD dates, treating them as YYYY-DD-MM instead.

It appears that the maintainers consider the `dayfirst` option to have been a mis-step, and a replacement for it has been coming Real Soon Now for the last 5 years, which isn't much consolation for developers who are quite happy with the principle of `dayfirst` and just want it to work.

`europarse` is a fork of the last good version of `dateutil.parser`, brought up to date with currently-supported versions of Python (3.7 to 3.11).

## Installation

```sh
pip install europarse
```

## Usage

```python
from europarse.parser import parse

parse("8th nov 2022")
# => datetime.datetime(2022, 11, 8, 0, 0)
```
