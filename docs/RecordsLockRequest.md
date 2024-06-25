# RecordsLockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**List[RecordLockID]**](RecordLockID.md) |  | [optional] 

## Example

```python
from grax.models.records_lock_request import RecordsLockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordsLockRequest from a JSON string
records_lock_request_instance = RecordsLockRequest.from_json(json)
# print the JSON string representation of the object
print(RecordsLockRequest.to_json())

# convert the object into a dict
records_lock_request_dict = records_lock_request_instance.to_dict()
# create an instance of RecordsLockRequest from a dict
records_lock_request_from_dict = RecordsLockRequest.from_dict(records_lock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


