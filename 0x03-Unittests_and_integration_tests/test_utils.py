#!/usr/bin/env python3
"""
unit test for utils.access_nested_map
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """
    Test cases for access_nested_map func
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
        ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected_result: int):
        """
        Test access_nested_map function with various inputs

        Args:
            nested_map: nested map to test
            path: path to access within the nested map
            expected_result: expected result after accessing the path
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"]),
        ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence):
        """
        Test that KeyError is raised for some inputs

        Args:
            nested_map: nested map to test
            path: Path to access within the nested map
            expected_exeception: expected exception result
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)
