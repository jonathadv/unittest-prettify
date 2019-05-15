# unittest prettify

[![license](https://img.shields.io/pypi/l/unittest-prettify.svg)](https://pypi.org/project/unittest-prettify/)
[![pypi version](https://img.shields.io/pypi/v/unittest-prettify.svg)](https://pypi.org/project/unittest-prettify/)
[![python versions](https://img.shields.io/pypi/pyversions/unittest-prettify.svg)](https://pypi.org/project/unittest-prettify/)
[![Build Status](https://travis-ci.org/jonathadv/unittest-prettify.svg?branch=master)](https://travis-ci.org/jonathadv/unittest-prettify)
[![Code covarage](https://codecov.io/gh/jonathadv/unittest-prettify/branch/master/graph/badge.svg)](https://codecov.io/gh/jonathadv/unittest-prettify)

A simple module to improve the [unittest](https://docs.python.org/3/library/unittest.html) output.




### Which unittest output do you prefer?
|    |    |
|----|----|
|<img src="https://github.com/jonathadv/unittest-prettify/raw/master/assets/screenshot1.png" width="300"> |<img src="https://github.com/jonathadv/unittest-prettify/raw/master/assets/screenshot2.png" width="300"> |

If you prefer the one in the right side, this module is for you.

**unittest prettify** aims to be a set of tools to improve the `unittest` lib output.

**Main features**
- Change the test description color in both class and method levels.
- Support to libraries which use `unittest` as bese such as [Django](https://docs.djangoproject.com/en/dev/topics/testing/overview/).


## Installing it
```
pip install unittest-prettify 
```

## Using it

#### Changing the color for a whole test case:
The `test_1()` and `test_2()` will inherit the green color from the class definition. 

```python
import unittest
from unittest_prettify.colorize import (
    colorize,
    GREEN,
)

@colorize(color=GREEN)
class Foo(unittest.TestCase):
    def test_1(self):
        """This test comment should be with the Class color set as GREEN"""

    def test_2(self):
        """This test comment should be with the Class color set as GREEN"""

```

#### Changing the color for a specific test:
The `test_1()` will inherit the green color from the class definition, but `test_2()` will overwrite the color by red.

```python
import unittest
from unittest_prettify.colorize import (
    colorize,
    GREEN,
    RED,
)

@colorize(color=GREEN)
class Foo(unittest.TestCase):
    def test_1(self):
        """This test comment should be with the Class color set as GREEN"""
        
    @colorize(color=RED)
    def test_2(self):
        """This test comment should be RED"""

``` 