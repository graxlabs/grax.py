# LockObjectRecordsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**List[RecordLockID]**](RecordLockID.md) | Record IDs to lock. | [optional] 

## Example

```python
from grax.models.lock_object_records_schema import LockObjectRecordsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LockObjectRecordsSchema from a JSON string
lock_object_records_schema_instance = LockObjectRecordsSchema.from_json(json)
# print the JSON string representation of the object
print(LockObjectRecordsSchema.to_json())

# convert the object into a dict
lock_object_records_schema_dict = lock_object_records_schema_instance.to_dict()
# create an instance of LockObjectRecordsSchema from a dict
lock_object_records_schema_from_dict = LockObjectRecordsSchema.from_dict(lock_object_records_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


