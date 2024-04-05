# DeletionCaller


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, List[str]]** |  | [optional] 
**remote_addr** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from grax.models.deletion_caller import DeletionCaller

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionCaller from a JSON string
deletion_caller_instance = DeletionCaller.from_json(json)
# print the JSON string representation of the object
print(DeletionCaller.to_json())

# convert the object into a dict
deletion_caller_dict = deletion_caller_instance.to_dict()
# create an instance of DeletionCaller from a dict
deletion_caller_form_dict = deletion_caller.from_dict(deletion_caller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


