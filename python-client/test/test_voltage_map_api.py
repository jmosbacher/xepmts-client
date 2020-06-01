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
from xepmts.api.voltage_map_api import VoltageMapApi  # noqa: E501
from xepmts.rest import ApiException


class TestVoltageMapApi(unittest.TestCase):
    """VoltageMapApi unit test stubs"""

    def setUp(self):
        self.api = xepmts.api.voltage_map_api.VoltageMapApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_voltage_map_item(self):
        """Test case for delete_voltage_map_item

        Deletes a VoltageMap document  # noqa: E501
        """
        pass

    def test_delete_voltage_maps(self):
        """Test case for delete_voltage_maps

        Deletes all VoltageMaps  # noqa: E501
        """
        pass

    def test_get_voltage_map_item(self):
        """Test case for get_voltage_map_item

        Retrieves a VoltageMap document  # noqa: E501
        """
        pass

    def test_get_voltage_map_item_by_name(self):
        """Test case for get_voltage_map_item_by_name

        Retrieves a VoltageMap document by name  # noqa: E501
        """
        pass

    def test_get_voltage_maps(self):
        """Test case for get_voltage_maps

        Retrieves one or more VoltageMaps  # noqa: E501
        """
        pass

    def test_post_voltage_maps(self):
        """Test case for post_voltage_maps

        Stores one or more VoltageMaps.  # noqa: E501
        """
        pass

    def test_put_voltage_map_item(self):
        """Test case for put_voltage_map_item

        Replaces a VoltageMap document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()