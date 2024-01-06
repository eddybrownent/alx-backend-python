#!/usr/bin/env python3
"""
Tests that GithubOrgClient.org returns the correct value
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
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

    def test_public_repos_url(self):
        """
        Test GithubOrgClient._public_repos_url returns the correct value

        Args:
            mock_org: Mock object for the org method
        """
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                    'repos_url': "https://api.github.com/users/google/repos"}
            github_org_client = GithubOrgClient("google")

            result = github_org_client._public_repos_url

            expected_result = "https://api.github.com/users/google/repos"
            self.assertEqual(result, expected_result)
