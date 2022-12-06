# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import ev3api
from ev3api.paths.motor_tacho import post  # noqa: E501
from ev3api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestMotorTacho(ApiTestMixin, unittest.TestCase):
    """
    MotorTacho unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''




if __name__ == '__main__':
    unittest.main()
