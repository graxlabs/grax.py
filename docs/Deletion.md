# Deletion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caller** | [**DeletionCaller**](DeletionCaller.md) |  | [optional] 
**cascade** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**force_cascade_objects** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**skip_deleted_check** | **bool** |  | [optional] 

## Example

```python
from grax.models.deletion import Deletion

# TODO update the JSON string below
json = "{}"
# create an instance of Deletion from a JSON string
deletion_instance = Deletion.from_json(json)
# print the JSON string representation of the object
print(Deletion.to_json())

# convert the object into a dict
deletion_dict = deletion_instance.to_dict()
# create an instance of Deletion from a dict
deletion_form_dict = deletion.from_dict(deletion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


