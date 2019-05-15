import sys
import unittest
from contextlib import contextmanager
from io import StringIO

from unittest_prettify.colorize import (
    BLUE,
    GREEN,
    MAGENTA,
    RED,
    RESET,
    WHITE,
    YELLOW,
    colorize,
)


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def _extract_test_comment(stderr):
    value = stderr.getvalue().strip()
    value = value.split("\n")[1]
    value = value.replace("... ok", "").strip()
    return value


class Test:
    @colorize(color=GREEN)
    class ColorizedClass(unittest.TestCase):
        @colorize(color=WHITE)
        def test_white(self):
            """This test comment should be WHITE"""

        @colorize(color=RED)
        def test_red(self):
            """This test comment should be RED"""

        @colorize(color=BLUE)
        def test_blue(self):
            """This test comment should be BLUE"""

        @colorize(color=MAGENTA)
        def test_magenta(self):
            """This test comment should be MAGENTA"""

        @colorize(color=YELLOW)
        def test_yellow(self):
            """This test comment should be YELLOW"""

        def test_green1(self):
            """This test comment should be with the default color set as GREEN"""

    class NotColorizedClass(unittest.TestCase):
        def test_no_color(self):
            """This test comment should not have color"""

        @colorize(color=BLUE)
        def test_blue(self):
            """This test comment should be BLUE"""

        @colorize(color=RED)
        def test_red(self):
            """This test comment should be RED"""

    @colorize(color=GREEN)
    class NoCommentClass(unittest.TestCase):
        def test_with_no_comment(self):
            pass


class ColorizedClassTestCase(unittest.TestCase):
    tests = (
        {
            "name": "test_white",
            "comment": "This test comment should be WHITE",
            "color": WHITE,
        },
        {
            "name": "test_red",
            "comment": "This test comment should be RED",
            "color": RED,
        },
        {
            "name": "test_blue",
            "comment": "This test comment should be BLUE",
            "color": BLUE,
        },
        {
            "name": "test_magenta",
            "comment": "This test comment should be MAGENTA",
            "color": MAGENTA,
        },
        {
            "name": "test_yellow",
            "comment": "This test comment should be YELLOW",
            "color": YELLOW,
        },
        {
            "name": "test_green1",
            "comment": "This test comment should be with the default color set as GREEN",
            "color": GREEN,
        },
    )

    def test_colorized_class(self):
        """Should match all test description colors against the @colorize decorator in method or in the class"""
        for test in self.tests:
            with captured_output() as (_, err):
                suite = unittest.TestSuite([Test.ColorizedClass(test["name"])])
                unittest.TextTestRunner(verbosity=2).run(suite)
            current_value = _extract_test_comment(err)
            expected_value = f"{test['color']}{test['comment']}{RESET}"

            self.assertEqual(current_value, expected_value)


class ColorizedMethodsOnlyTestCase(unittest.TestCase):
    tests = (
        {
            "name": "test_blue",
            "comment": "This test comment should be BLUE",
            "color": BLUE,
        },
        {
            "name": "test_red",
            "comment": "This test comment should be RED",
            "color": RED,
        },
    )

    def test_colorized_methods(self):
        """Should match all test description colors against the @colorize decorator in the mothod"""
        for test in self.tests:
            with captured_output() as (_, err):
                suite = unittest.TestSuite([Test.NotColorizedClass(test["name"])])
                unittest.TextTestRunner(verbosity=2).run(suite)
            current_value = _extract_test_comment(err)
            expected_value = f"{test['color']}{test['comment']}{RESET}"

            self.assertEqual(current_value, expected_value)

    def test_not_colorized_method(self):
        """Method without @colorize should not have color"""
        with captured_output() as (_, err):
            suite = unittest.TestSuite([Test.NotColorizedClass("test_no_color")])
            unittest.TextTestRunner(verbosity=2).run(suite)
        current_value = _extract_test_comment(err)
        expected_value = "This test comment should not have color"

        self.assertEqual(current_value, expected_value)


class NoCommentTestCase(unittest.TestCase):
    def test_not_commented_method(self):
        """Should not throw error even if there is not comment in the method"""
        with captured_output() as (_, err):
            suite = unittest.TestSuite([Test.NoCommentClass("test_with_no_comment")])
            unittest.TextTestRunner(verbosity=2).run(suite)
        current_value = _extract_test_comment(err)

        self.assertEqual(current_value, "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
