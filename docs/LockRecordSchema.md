# LockRecordSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Note about the lock. | [optional] 

## Example

```python
from grax.models.lock_record_schema import LockRecordSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LockRecordSchema from a JSON string
lock_record_schema_instance = LockRecordSchema.from_json(json)
# print the JSON string representation of the object
print(LockRecordSchema.to_json())

# convert the object into a dict
lock_record_schema_dict = lock_record_schema_instance.to_dict()
# create an instance of LockRecordSchema from a dict
lock_record_schema_from_dict = LockRecordSchema.from_dict(lock_record_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


