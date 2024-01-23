# coding: utf-8

"""
    FormKiQ HTTP API

    Formkiq API: Document Management Platform API using OAuth(JWT) Authentication  You can find out more about FormKiQ at [https://formkiq.com](http://formkiq.com).  ## Introduction  FormKiQ is an API-first (head-less), battle-tested document management API. The FormKiQ API provides all the API endpoints to build your Perfect Document Management Platform.  FormKiQ API was built on top of [OpenAPI specification](https://www.openapis.org), so it is easy to use the API spec file with any application that supports the OpenAPI specification.  Open API OAuth Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml  Open API IAM Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-iam.yaml  ## Authentication FormKiQ offers three forms of authentication:   - OAuth(JWT)   - AWS IAM   - API Key

    The version of the OpenAPI document: 1.13.0
    Contact: support@formkiq.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from formkiq_client.api.user_management_api import UserManagementApi


class TestUserManagementApi(unittest.TestCase):
    """UserManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserManagementApi()

    def tearDown(self) -> None:
        pass

    def test_get_groups(self) -> None:
        """Test case for get_groups

        Get configured system group(s)
        """
        pass

    def test_get_users_in_group(self) -> None:
        """Test case for get_users_in_group

        Get users in a group
        """
        pass


if __name__ == '__main__':
    unittest.main()