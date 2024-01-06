#!/usr/bin/env python3
"""
Tests that GithubOrgClient.org returns the correct value
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test for the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
        ])
    @patch('client.get_json', return_value={"name": "mocked_org"})
    def test_org(self, org_name: str, mock_get_json: MagicMock):
        """
        Test GithubOrgClient.org returns the correct value

        Args:
            org_name : name of GitHub organization
            mock_get_json : Mock object for get_json func
        """
        github_org_client = GithubOrgClient(org_name)

        result = github_org_client.org

        mock_get_json.assert_called_once_with(
                GithubOrgClient.ORG_URL.format(org=org_name))

        self.assertEqual(result, {"name": "mocked_org"})
