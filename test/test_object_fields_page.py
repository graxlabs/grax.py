# coding: utf-8

"""
    GRAX API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from grax.models.object_fields_page import ObjectFieldsPage

class TestObjectFieldsPage(unittest.TestCase):
    """ObjectFieldsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObjectFieldsPage:
        """Test ObjectFieldsPage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObjectFieldsPage`
        """
        model = ObjectFieldsPage()
        if include_optional:
            return ObjectFieldsPage(
                fields = [
                    grax.models.object_field.ObjectField(
                        label = '', 
                        name = '', 
                        name_field = True, 
                        type = '', )
                    ],
                next_page_token = ''
            )
        else:
            return ObjectFieldsPage(
        )
        """

    def testObjectFieldsPage(self):
        """Test ObjectFieldsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()