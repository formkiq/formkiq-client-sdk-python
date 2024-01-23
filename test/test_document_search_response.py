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
import datetime

from formkiq_client.models.document_search_response import DocumentSearchResponse

class TestDocumentSearchResponse(unittest.TestCase):
    """DocumentSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentSearchResponse:
        """Test DocumentSearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentSearchResponse`
        """
        model = DocumentSearchResponse()
        if include_optional:
            return DocumentSearchResponse(
                next = '',
                previous = '',
                documents = [
                    formkiq_client.models.search_result_document.SearchResultDocument(
                        site_id = '', 
                        path = '', 
                        deep_link_path = '', 
                        inserted_date = '', 
                        last_modified_date = '', 
                        folder = True, 
                        index_key = '', 
                        checksum = '', 
                        document_id = '', 
                        content_type = '', 
                        user_id = '', 
                        content_length = 56, 
                        version_id = '', 
                        belongs_to_document_id = '', 
                        matched_tag = formkiq_client.models.document_search_match_tag.DocumentSearchMatchTag(
                            key = '', 
                            value = '', 
                            type = '', ), 
                        matched_tags = [
                            formkiq_client.models.document_search_match_tag.DocumentSearchMatchTag(
                                key = '', 
                                value = '', 
                                type = '', )
                            ], 
                        tags = { }, 
                        metadata = [
                            formkiq_client.models.document_metadata.DocumentMetadata(
                                key = '', 
                                value = '', 
                                values = [
                                    ''
                                    ], )
                            ], )
                    ]
            )
        else:
            return DocumentSearchResponse(
        )
        """

    def testDocumentSearchResponse(self):
        """Test DocumentSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
