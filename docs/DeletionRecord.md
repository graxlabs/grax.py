# DeletionRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**modified_at** | **datetime** |  | [optional] 
**object** | **str** |  | [optional] 
**purged_at** | **datetime** |  | [optional] 

## Example

```python
from grax.models.deletion_record import DeletionRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionRecord from a JSON string
deletion_record_instance = DeletionRecord.from_json(json)
# print the JSON string representation of the object
print(DeletionRecord.to_json())

# convert the object into a dict
deletion_record_dict = deletion_record_instance.to_dict()
# create an instance of DeletionRecord from a dict
deletion_record_from_dict = DeletionRecord.from_dict(deletion_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


