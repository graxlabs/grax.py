# ChildRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_source** | **str** | The delete source of the record, if it has been deleted. Can be &#39;grax&#39; or &#39;salesforce&#39;. | [optional] 
**deleted_at** | **datetime** | The time the record was deleted, if it has been deleted. | [optional] 
**fields** | **Dict[str, str]** | The fields of the record, if requested. | [optional] 
**id** | **str** | The ID of the record. | [optional] 
**modified_at** | **datetime** | The time the record was last modified. | [optional] 
**name** | **str** | The name of the record, if requested. | [optional] 
**object** | **str** | The object of the record. | [optional] 
**salesforce_url** | **str** | The Salesforce URL of the record. | [optional] 

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
child_record_form_dict = child_record.from_dict(child_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


