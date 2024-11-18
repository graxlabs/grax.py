# RecordLockID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from grax.models.record_lock_id import RecordLockID

# TODO update the JSON string below
json = "{}"
# create an instance of RecordLockID from a JSON string
record_lock_id_instance = RecordLockID.from_json(json)
# print the JSON string representation of the object
print(RecordLockID.to_json())

# convert the object into a dict
record_lock_id_dict = record_lock_id_instance.to_dict()
# create an instance of RecordLockID from a dict
record_lock_id_from_dict = RecordLockID.from_dict(record_lock_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


