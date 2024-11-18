# ChildRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_source** | **str** | Delete source of the record, if it has been deleted. Can be &#39;grax&#39; or &#39;salesforce&#39;. | [optional] 
**deleted_at** | **datetime** | Time the record was deleted, if it has been deleted. | [optional] 
**fields** | **Dict[str, str]** | Fields of the record, if requested. | [optional] 
**id** | **str** | Record ID. | [optional] 
**modified_at** | **datetime** | Time the record was last modified. | [optional] 
**name** | **str** | Name of the record, if requested. | [optional] 
**object** | **str** | Object of the record. | [optional] 
**salesforce_url** | **str** | Salesforce URL for the record. | [optional] 

## Example

```python
from grax.models.child_record import ChildRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ChildRecord from a JSON string
child_record_instance = ChildRecord.from_json(json)
# print the JSON string representation of the object
print(ChildRecord.to_json())

# convert the object into a dict
child_record_dict = child_record_instance.to_dict()
# create an instance of ChildRecord from a dict
child_record_from_dict = ChildRecord.from_dict(child_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


