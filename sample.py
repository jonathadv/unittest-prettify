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


@colorize(color=GREEN)
class Foo(unittest.TestCase):
    def test_1(self):
        """This test comment should be with the Class color set as GREEN"""

    def test_2(self):
        """This test comment should be with the Class color set as GREEN"""


@colorize(color=GREEN)
class Bar(unittest.TestCase):
    @colorize(color=WHITE)
    def test_1(self):
        """This test comment should be WHITE"""

    @colorize(color=RED)
    def test_2(self):
        """This test comment should be RED"""

    @colorize(color=BLUE)
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
