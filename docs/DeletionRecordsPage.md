# DeletionRecordsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Token to retrieve the next page of results, blank if done. | [optional] 
**records** | [**List[DeletionRecord]**](DeletionRecord.md) |  | [optional] 

## Example

```python
from grax.models.deletion_records_page import DeletionRecordsPage

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionRecordsPage from a JSON string
deletion_records_page_instance = DeletionRecordsPage.from_json(json)
# print the JSON string representation of the object
print(DeletionRecordsPage.to_json())

# convert the object into a dict
deletion_records_page_dict = deletion_records_page_instance.to_dict()
# create an instance of DeletionRecordsPage from a dict
deletion_records_page_form_dict = deletion_records_page.from_dict(deletion_records_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


