# coding: utf-8

"""
    FormKiQ API

    Formkiq API: Document Management Platform API using OAuth(JWT) Authentication  You can find out more about FormKiQ at [https://formkiq.com](http://formkiq.com).  ## Introduction  FormKiQ is an API-first (head-less), battle-tested document management API. The FormKiQ API provides all the API endpoints to build your Perfect Document Management Platform.  FormKiQ API was built on top of [OpenAPI specification](https://www.openapis.org), so it is easy to use the API spec file with any application that supports the OpenAPI specification.  Open API OAuth Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml  Open API IAM Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-iam.yaml  ## Authentication FormKiQ offers three forms of authentication:   - OAuth(JWT)   - AWS IAM   - API Key

    The version of the OpenAPI document: 1.14.0
    Contact: support@formkiq.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from formkiq_client.api.rulesets_api import RulesetsApi


class TestRulesetsApi(unittest.TestCase):
    """RulesetsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RulesetsApi()

    def tearDown(self) -> None:
        pass

    def test_add_rule(self) -> None:
        """Test case for add_rule

        Add New Rule
        """
        pass

    def test_add_ruleset(self) -> None:
        """Test case for add_ruleset

        Add New Ruleset
        """
        pass

    def test_delete_rule(self) -> None:
        """Test case for delete_rule

        Delete Rule
        """
        pass

    def test_delete_ruleset(self) -> None:
        """Test case for delete_ruleset

        Delete Ruleset
        """
        pass

    def test_get_rule(self) -> None:
        """Test case for get_rule

        Get Rule
        """
        pass

    def test_get_rules(self) -> None:
        """Test case for get_rules

        Get Rules
        """
        pass

    def test_get_ruleset(self) -> None:
        """Test case for get_ruleset

        Get Ruleset
        """
        pass

    def test_get_rulesets(self) -> None:
        """Test case for get_rulesets

        Get Rulesets
        """
        pass

    def test_update_rule(self) -> None:
        """Test case for update_rule

        Update Rule
        """
        pass

    def test_update_ruleset(self) -> None:
        """Test case for update_ruleset

        Update Ruleset
        """
        pass


if __name__ == '__main__':
    unittest.main()