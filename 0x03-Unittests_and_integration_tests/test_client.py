#!/usr/bin/env python3
"""
Tests that GithubOrgClient.org returns the correct value
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


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

    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    @patch('client.get_json')
    def test_public_repos(self,
                          mock_get_json: MagicMock,
                          mock_pub_url: PropertyMock):
        """
        Test public_repos method
        """
        mock_get_json.return_value = [
                {"name": "projectA", "license": {"key": "apache"}},
                {"name": "projectB", "license": {"key": "mit"}},
                {"name": "projectC", "license": {"key": "gpl"}},
                ]

        mock_pub_url.return_value = "https://api.github.com/orgs/google/repos"

        github_org_client = GithubOrgClient("google")

        repos = github_org_client.public_repos(license="mit")

        expected_repos = ["projectB"]
        self.assertEqual(repos, expected_repos)

        mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos")

        mock_pub_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "owned_license"}}, "owned_license", True),
        ({"license": {"key": "new_license"}}, "owned_license", False),
        ])
    def test_has_license(self, repo: Dict, license_key: str,
                         expected_result: bool):
        """
        Tests the has_license method
        """
        github_org_client = GithubOrgClient("testorg")

        result = github_org_client.has_license(repo, license_key)

        self.assertEqual(result, expected_result)
