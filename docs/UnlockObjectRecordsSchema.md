# UnlockObjectRecordsSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** | Record IDs to unlock. | [optional] 

## Example

```python
from grax.models.unlock_object_records_schema import UnlockObjectRecordsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UnlockObjectRecordsSchema from a JSON string
unlock_object_records_schema_instance = UnlockObjectRecordsSchema.from_json(json)
# print the JSON string representation of the object
print(UnlockObjectRecordsSchema.to_json())

# convert the object into a dict
unlock_object_records_schema_dict = unlock_object_records_schema_instance.to_dict()
# create an instance of UnlockObjectRecordsSchema from a dict
unlock_object_records_schema_from_dict = UnlockObjectRecordsSchema.from_dict(unlock_object_records_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


