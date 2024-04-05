# RecordDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | ID of the activity that deleted the record. | [optional] 
**source** | **str** | Source of the delete. | [optional] 
**time** | **datetime** | Time the record was deleted. | [optional] 
**user** | [**AuditUser**](AuditUser.md) |  | [optional] 

## Example

```python
from grax.models.record_deleted import RecordDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of RecordDeleted from a JSON string
record_deleted_instance = RecordDeleted.from_json(json)
# print the JSON string representation of the object
print(RecordDeleted.to_json())

# convert the object into a dict
record_deleted_dict = record_deleted_instance.to_dict()
# create an instance of RecordDeleted from a dict
record_deleted_form_dict = record_deleted.from_dict(record_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


