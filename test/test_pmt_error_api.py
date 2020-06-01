# coding: utf-8

"""
    PMT API

    API for the XenonnT PMT database  # noqa: E501

    The version of the OpenAPI document: 0.1
    Contact: joe.mosbacher@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import xepmts
from xepmts.api.pmt_error_api import PmtErrorApi  # noqa: E501
from xepmts.rest import ApiException


class TestPmtErrorApi(unittest.TestCase):
    """PmtErrorApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.pmt_error_api.PmtErrorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_pmt_error_item(self):
        """Test case for delete_pmt_error_item

        Deletes a PmtError document  # noqa: E501
        """
        pass

    def test_get_pmt_error_item(self):
        """Test case for get_pmt_error_item

        Retrieves a PmtError document  # noqa: E501
        """
        pass

    def test_get_pmt_errors(self):
        """Test case for get_pmt_errors

        Retrieves one or more PmtErrors  # noqa: E501
        """
        pass

    def test_post_pmt_errors(self):
        """Test case for post_pmt_errors

        Stores one or more PmtErrors.  # noqa: E501
        """
        pass

    def test_put_pmt_error_item(self):
        """Test case for put_pmt_error_item

        Replaces a PmtError document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
