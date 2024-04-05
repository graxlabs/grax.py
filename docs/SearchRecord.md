# SearchRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Time the record was created. | [optional] 
**deleted** | [**RecordDeleted**](RecordDeleted.md) |  | [optional] 
**fields** | [**List[RecordField]**](RecordField.md) | Record fields. | [optional] 
**id** | **str** | Record ID. | [optional] 
**modified** | **datetime** | Time the record was modified. | [optional] 
**name** | **str** | Record name. | [optional] 
**purged** | [**RecordPurged**](RecordPurged.md) |  | [optional] 
**restored_from** | [**RecordRestoredFrom**](RecordRestoredFrom.md) |  | [optional] 
**salesforce_url** | **str** | Salesforce URL for the record. | [optional] 

## Example

```python
from grax.models.search_record import SearchRecord

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRecord from a JSON string
search_record_instance = SearchRecord.from_json(json)
# print the JSON string representation of the object
print(SearchRecord.to_json())

# convert the object into a dict
search_record_dict = search_record_instance.to_dict()
# create an instance of SearchRecord from a dict
search_record_form_dict = search_record.from_dict(search_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


