# coding: utf-8

"""
    FormKiQ API JWT

    Formkiq API: Document Management Platform API using OAuth(JWT) Authentication  You can find out more about FormKiQ at [https://formkiq.com](http://formkiq.com).  ## Introduction  FormKiQ is an API-first (head-less), battle-tested document management API. The FormKiQ API provides all the API endpoints to build your Perfect Document Management Platform.  FormKiQ API was built on top of [OpenAPI specification](https://www.openapis.org), so it is easy to use the API spec file with any application that supports the OpenAPI specification.  Open API OAuth Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-jwt.yaml  Open API IAM Specification - https://raw.githubusercontent.com/formkiq/formkiq-core/master/docs/openapi/openapi-iam.yaml  ## Authentication FormKiQ offers three forms of authentication:   - OAuth(JWT)   - AWS IAM   - API Key

    The version of the OpenAPI document: 1.17.0
    Contact: support@formkiq.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from formkiq_client.models.get_locale_resource_items_response import GetLocaleResourceItemsResponse

class TestGetLocaleResourceItemsResponse(unittest.TestCase):
    """GetLocaleResourceItemsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLocaleResourceItemsResponse:
        """Test GetLocaleResourceItemsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLocaleResourceItemsResponse`
        """
        model = GetLocaleResourceItemsResponse()
        if include_optional:
            return GetLocaleResourceItemsResponse(
                next = '',
                resource_items = [
                    formkiq_client.models.resource_item.ResourceItem(
                        item_type = 'INTERFACE', 
                        localized_value = '', 
                        interface_key = '', 
                        item_key = '', 
                        attribute_key = '', 
                        allowed_value = '', 
                        classification_id = '', )
                    ]
            )
        else:
            return GetLocaleResourceItemsResponse(
        )
        """

    def testGetLocaleResourceItemsResponse(self):
        """Test GetLocaleResourceItemsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
