import unittest
from unittest_prettify.colorize import (
    colorize,
    GREEN,
    WHITE,
    RED,
    BLUE,
    MAGENTA,
    YELLOW,
)


class Foo(unittest.TestCase):
    def test_1(self):
        """This test comment should be with the Class color set as GREEN"""

    def test_2(self):
        """This test comment should be with the Class color set as GREEN"""


class Bar(unittest.TestCase):

    def test_1(self):
        """This test comment should be WHITE"""


    def test_2(self):
        """This test comment should be RED"""


    def test_3(self):
        """This test comment should be BLUE"""

    @colorize(color=MAGENTA)
    def test_4(self):
        """This test comment should be MAGENTA"""

    @colorize(color=YELLOW)
    def test_5(self):
        """This test comment should be YELLOW"""

    def test_6(self):
        """This test comment should be with the Class color set as GREEN"""

    def test_7(self):
        """This test comment should be with the Class color set as GREEN"""


class FooBar(unittest.TestCase):
    @colorize(color=RED)
    def test_1(self):
        """This test comment should be RED"""

    @colorize(color=BLUE)
    def test_2(self):
        """This test comment should be BLUE"""

    @colorize(color=MAGENTA)
    def test_3(self):
        """This test comment should be MAGENTA"""

    def test_4(self):
        """This test comment should not have color"""

    def test_5(self):
        """This test comment should not have color"""


if __name__ == "__main__":
    unittest.main(verbosity=2)
