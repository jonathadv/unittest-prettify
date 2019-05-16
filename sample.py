import unittest
from unittest_prettify import prettify
from unittest_prettify.colors import RED
from unittest_prettify.templates import STAR


@prettify(template=STAR, color=RED)
class Foo(unittest.TestCase):
    @unittest.skip("why I want")
    def test_1(self):
        """This test comment should be with the Class color set as RED"""

    def test_2(self):
        """This test comment should be with the Class color set as GREEN"""


if __name__ == "__main__":
    unittest.main(verbosity=2)
