# Record


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | [**RecordDeleted**](RecordDeleted.md) |  | [optional] 
**fields** | [**List[RecordField]**](RecordField.md) | Record fields. | [optional] 
**id** | **str** | Record ID. | [optional] 
**modified** | **datetime** | Time the record was modified. | [optional] 
**name** | **str** | Record name. | [optional] 
**object** | **str** | Object name. | [optional] 
**purged** | [**RecordPurged**](RecordPurged.md) |  | [optional] 
**restored_from** | [**RecordRestoredFrom**](RecordRestoredFrom.md) |  | [optional] 
**salesforce_url** | **str** | Salesforce URL for the record. | [optional] 

## Example

```python
from grax.models.record import Record

# TODO update the JSON string below
json = "{}"
# create an instance of Record from a JSON string
record_instance = Record.from_json(json)
# print the JSON string representation of the object
print(Record.to_json())

# convert the object into a dict
record_dict = record_instance.to_dict()
# create an instance of Record from a dict
record_form_dict = record.from_dict(record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


