# coding: utf-8

"""
    FormKiQ API

    Formkiq API: Document Management Platform API using OAuth(JWT) Authentication  You can find out more about FormKiQ at [https://formkiq.com](http://formkiq.com).  ## Introduction  FormKiQ is an API-first (head-less), battle-tested document management API. The FormKiQ API provides all the API endpoints to build your Perfect Document Management Platform.  FormKiQ API was built on top of [OpenAPI specification](https://www.openapis.org), so it is easy to use the API spec file with any application that supports the OpenAPI specification.  Open API OAuth Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml  Open API IAM Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-iam.yaml  ## Authentication FormKiQ offers three forms of authentication:   - OAuth(JWT)   - AWS IAM   - API Key

    The version of the OpenAPI document: 1.15.0
    Contact: support@formkiq.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from formkiq_client.api.schemas_api import SchemasApi


class TestSchemasApi(unittest.TestCase):
    """SchemasApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SchemasApi()

    def tearDown(self) -> None:
        pass

    def test_add_classification(self) -> None:
        """Test case for add_classification

        Add Classification
        """
        pass

    def test_delete_classification(self) -> None:
        """Test case for delete_classification

        Delete Classification
        """
        pass

    def test_get_classification(self) -> None:
        """Test case for get_classification

        Get Classification
        """
        pass

    def test_get_sites_classifications(self) -> None:
        """Test case for get_sites_classifications

        Get Sites Classifications
        """
        pass

    def test_get_sites_schema(self) -> None:
        """Test case for get_sites_schema

        Get Sites Schema
        """
        pass

    def test_set_classification(self) -> None:
        """Test case for set_classification

        Set Classification
        """
        pass

    def test_set_sites_schema(self) -> None:
        """Test case for set_sites_schema

        Set Sites Schema
        """
        pass


if __name__ == '__main__':
    unittest.main()
