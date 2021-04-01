"""Test cases for the pipeline-based implementation"""

import pytest

from termfrequency import compute_tf_pipeline


# TODO: All additional test cases, with the goal of achieving high coverage

def test_read_file_populates_data():
    """Checks that the reading of the file works"""
    collected_data = compute_tf_pipeline.read_file("inputs/input.txt")
    assert collected_data


# TODO: Whenever possible, please use parameterized testing for your tests

@pytest.mark.parametrize(
    "input_string,expected_count",
    [("hello world", 2), ("hello world example", 3), ("", 0), (" ", 0), ("  ", 0)],
)
def test_scan_splits_string_correctly(input_string, expected_count):
    """Checks that scan function finds the correct number of words in the String"""
    assert len(compute_tf_pipeline.scan(input_string)) == expected_count
