# RecordsUnlockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 

## Example

```python
from grax.models.records_unlock_request import RecordsUnlockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordsUnlockRequest from a JSON string
records_unlock_request_instance = RecordsUnlockRequest.from_json(json)
# print the JSON string representation of the object
print(RecordsUnlockRequest.to_json())

# convert the object into a dict
records_unlock_request_dict = records_unlock_request_instance.to_dict()
# create an instance of RecordsUnlockRequest from a dict
records_unlock_request_from_dict = RecordsUnlockRequest.from_dict(records_unlock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


