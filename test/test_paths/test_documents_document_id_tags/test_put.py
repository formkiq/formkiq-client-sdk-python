# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import formkiq_client
from formkiq_client.paths.documents_document_id_tags import put  # noqa: E501
from formkiq_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDocumentsDocumentIdTags(ApiTestMixin, unittest.TestCase):
    """
    DocumentsDocumentIdTags unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
