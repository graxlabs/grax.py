# coding: utf-8

"""
    GRAX API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from grax.models.search_records_page import SearchRecordsPage

class TestSearchRecordsPage(unittest.TestCase):
    """SearchRecordsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchRecordsPage:
        """Test SearchRecordsPage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchRecordsPage`
        """
        model = SearchRecordsPage()
        if include_optional:
            return SearchRecordsPage(
                next_continue_page_token = '',
                next_page_token = '',
                records = [
                    grax.models.search_record.SearchRecord(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        deleted = grax.models.record_deleted.RecordDeleted(
                            activity_id = '', 
                            source = 'grax', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            user = grax.models.audit_user.AuditUser(
                                email = '', 
                                id = '', 
                                name = '', ), ), 
                        fields = [
                            grax.models.record_field.RecordField(
                                name = '', 
                                value = '', )
                            ], 
                        id = '', 
                        modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        purged = grax.models.record_purged.RecordPurged(
                            activity_id = '', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        restored_from = grax.models.record_restored_from.RecordRestoredFrom(
                            activity_id = '', 
                            added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = '', 
                            modified = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                        salesforce_url = '', )
                    ]
            )
        else:
            return SearchRecordsPage(
        )
        """

    def testSearchRecordsPage(self):
        """Test SearchRecordsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
