# RecordRestoredFrom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | Activity ID that restored the record. | [optional] 
**added** | **datetime** | Added time of the new record. | [optional] 
**id** | **str** | ID of the original record. | [optional] 
**modified** | **datetime** | Modified time of the original record. | [optional] 
**user** | [**AuditUser**](AuditUser.md) |  | [optional] 

## Example

```python
from grax.models.record_restored_from import RecordRestoredFrom

# TODO update the JSON string below
json = "{}"
# create an instance of RecordRestoredFrom from a JSON string
record_restored_from_instance = RecordRestoredFrom.from_json(json)
# print the JSON string representation of the object
print(RecordRestoredFrom.to_json())

# convert the object into a dict
record_restored_from_dict = record_restored_from_instance.to_dict()
# create an instance of RecordRestoredFrom from a dict
record_restored_from_form_dict = record_restored_from.from_dict(record_restored_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


