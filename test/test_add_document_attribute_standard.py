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

from formkiq_client.models.add_document_attribute_standard import AddDocumentAttributeStandard

class TestAddDocumentAttributeStandard(unittest.TestCase):
    """AddDocumentAttributeStandard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddDocumentAttributeStandard:
        """Test AddDocumentAttributeStandard
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddDocumentAttributeStandard`
        """
        model = AddDocumentAttributeStandard()
        if include_optional:
            return AddDocumentAttributeStandard(
                key = '',
                string_value = '',
                string_values = [
                    ''
                    ],
                number_value = 1.337,
                number_values = [
                    1.337
                    ],
                boolean_value = True
            )
        else:
            return AddDocumentAttributeStandard(
                key = '',
        )
        """

    def testAddDocumentAttributeStandard(self):
        """Test AddDocumentAttributeStandard"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
