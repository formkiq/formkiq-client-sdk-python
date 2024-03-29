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

from formkiq_client.api.advanced_document_search_api import AdvancedDocumentSearchApi


class TestAdvancedDocumentSearchApi(unittest.TestCase):
    """AdvancedDocumentSearchApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AdvancedDocumentSearchApi()

    def tearDown(self) -> None:
        pass

    def test_delete_document_fulltext(self) -> None:
        """Test case for delete_document_fulltext

        Delete document full-text
        """
        pass

    def test_delete_document_fulltext_tag(self) -> None:
        """Test case for delete_document_fulltext_tag

        Delete document full-text tag
        """
        pass

    def test_delete_document_fulltext_tag_and_value(self) -> None:
        """Test case for delete_document_fulltext_tag_and_value

        Delete document full-text tag/value
        """
        pass

    def test_document_fulltext(self) -> None:
        """Test case for document_fulltext

        Document full-text search
        """
        pass

    def test_get_document_fulltext(self) -> None:
        """Test case for get_document_fulltext

        Get document's full-text
        """
        pass

    def test_query_fulltext(self) -> None:
        """Test case for query_fulltext

        Direct opensearch search API
        """
        pass

    def test_set_document_fulltext(self) -> None:
        """Test case for set_document_fulltext

        Set document's full-text
        """
        pass

    def test_update_document_fulltext(self) -> None:
        """Test case for update_document_fulltext

        Update document's full-text
        """
        pass


if __name__ == '__main__':
    unittest.main()
