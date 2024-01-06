#!/usr/bin/env python3
"""
unit test for utils.access_nested_map
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import patch, Mock


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
        ({"a": 1}, ["a", "b"])
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


class TestGetJson(unittest.TestCase):
    """
    Test cases for the get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get: Mock):
        """
        Test that get_json returns the expected result

        Args:
            test_url: url to send the request
            payload: the expected json response
            mock_get: mock object to replace requests.get when testing
        """
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test cases for the memoize decorator
    """
    def test_memoize(self):
        """
        Test the memoize decorator
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_object:
            test_instance = TestClass()
            resultA = test_instance.a_property()
            resultB = test_instance.a_property()

            mock_object.assert_called_once()
