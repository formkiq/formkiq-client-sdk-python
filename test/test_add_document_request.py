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

from formkiq_client.models.add_document_request import AddDocumentRequest

class TestAddDocumentRequest(unittest.TestCase):
    """AddDocumentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddDocumentRequest:
        """Test AddDocumentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddDocumentRequest`
        """
        model = AddDocumentRequest()
        if include_optional:
            return AddDocumentRequest(
                tag_schema_id = '',
                path = '',
                deep_link_path = '',
                content_type = '',
                is_base64 = True,
                content = '',
                tags = [
                    formkiq_client.models.add_document_tag.AddDocumentTag(
                        key = '', 
                        value = '', 
                        values = [
                            ''
                            ], )
                    ],
                metadata = [
                    formkiq_client.models.add_document_metadata.AddDocumentMetadata(
                        key = '', 
                        value = '', 
                        values = [
                            ''
                            ], )
                    ],
                actions = [
                    formkiq_client.models.add_action.AddAction(
                        type = 'OCR', 
                        parameters = formkiq_client.models.add_action_parameters.AddActionParameters(
                            ocr_parse_types = '', 
                            ocr_engine = 'TESSERACT', 
                            add_pdf_detected_characters_as_text = True, 
                            url = '', 
                            character_max = '', 
                            engine = 'chatgpt', 
                            notification_type = 'email', 
                            notification_to_cc = '', 
                            notification_to_bcc = '', 
                            notification_subject = '', 
                            notification_text = '', 
                            notification_html = '', 
                            tags = '', 
                            queue_name = '', ), )
                    ],
                documents = [
                    formkiq_client.models.add_child_document.AddChildDocument(
                        path = '', 
                        deep_link_path = '', 
                        content_type = '', 
                        is_base64 = True, 
                        content = '', 
                        tags = [
                            formkiq_client.models.add_document_tag.AddDocumentTag(
                                key = '', 
                                value = '', 
                                values = [
                                    ''
                                    ], )
                            ], 
                        metadata = [
                            formkiq_client.models.add_document_metadata.AddDocumentMetadata(
                                key = '', 
                                value = '', )
                            ], )
                    ]
            )
        else:
            return AddDocumentRequest(
                content = '',
        )
        """

    def testAddDocumentRequest(self):
        """Test AddDocumentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
