# coding: utf-8

"""
    GRAX API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from grax.models.audit_user import AuditUser

class TestAuditUser(unittest.TestCase):
    """AuditUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuditUser:
        """Test AuditUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuditUser`
        """
        model = AuditUser()
        if include_optional:
            return AuditUser(
                email = '',
                id = '',
                name = ''
            )
        else:
            return AuditUser(
        )
        """

    def testAuditUser(self):
        """Test AuditUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
