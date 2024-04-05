# RecordPurged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** | ID of the activity that purged the record. | [optional] 
**time** | **datetime** | Time the record was purged. | [optional] 
**user** | [**AuditUser**](AuditUser.md) |  | [optional] 

## Example

```python
from grax.models.record_purged import RecordPurged

# TODO update the JSON string below
json = "{}"
# create an instance of RecordPurged from a JSON string
record_purged_instance = RecordPurged.from_json(json)
# print the JSON string representation of the object
print(RecordPurged.to_json())

# convert the object into a dict
record_purged_dict = record_purged_instance.to_dict()
# create an instance of RecordPurged from a dict
record_purged_form_dict = record_purged.from_dict(record_purged_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


