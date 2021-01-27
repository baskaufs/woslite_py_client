# coding: utf-8

"""
    Web of Science API Lite

    A responsive API that supports rich searching across the Web of Science Core Collection to retrieve core article metadata.  This service provides a great way to reuse Web of Science data both internally and externally to enhance  institutional repositories and research networking systems with best-in-class data. This API supports searching across the Web of Science to retrieve item-level metadata with limited fields:  - UT (Unique Identifier) - Authors - Author keywords - Document type - Title - Issue - Pages - Publication date - Source title - Volume - DOI - ISBN - ISSN   The API supports JSON and XML responses, and this documentation supports trying both response types.   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import woslite_client
from woslite_client.models.source import Source  # noqa: E501
from woslite_client.rest import ApiException


class TestSource(unittest.TestCase):
    """Source unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSource(self):
        """Test Source"""
        # FIXME: construct object with mandatory attributes with example values
        # model = woslite_client.models.source.Source()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()