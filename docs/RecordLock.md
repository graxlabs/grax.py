# RecordLock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locked** | **datetime** | Time the record was locked. If not present, the record is not locked. | [optional] 
**locked_id** | **str** | ID of the record causing this record to be locked | [optional] 
**note** | **str** | Note about the lock | [optional] 
**user_id** | **str** | ID of the user who locked the record | [optional] 

## Example

```python
from grax.models.record_lock import RecordLock

# TODO update the JSON string below
json = "{}"
# create an instance of RecordLock from a JSON string
record_lock_instance = RecordLock.from_json(json)
# print the JSON string representation of the object
print(RecordLock.to_json())

# convert the object into a dict
record_lock_dict = record_lock_instance.to_dict()
# create an instance of RecordLock from a dict
record_lock_form_dict = record_lock.from_dict(record_lock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


