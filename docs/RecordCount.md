# RecordCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** | Count of records created. Only applies to records with a CreatedDate field. | [optional] 
**deleted_by_grax** | **int** | Count of records archived with GRAX. | [optional] 
**deleted_by_source** | **int** | Count of records deleted directly in Salesforce. | [optional] 
**group** | **datetime** | Timestamp corresponding to the beginning of the group (hour, day, month or year), if any. | [optional] 
**modified** | **int** | Count of records modified; Does not consider records created and then modified in the group. | [optional] 
**object** | **str** | The object name; empty when representing all objects. | [optional] 

## Example

```python
from grax.models.record_count import RecordCount

# TODO update the JSON string below
json = "{}"
# create an instance of RecordCount from a JSON string
record_count_instance = RecordCount.from_json(json)
# print the JSON string representation of the object
print(RecordCount.to_json())

# convert the object into a dict
record_count_dict = record_count_instance.to_dict()
# create an instance of RecordCount from a dict
record_count_from_dict = RecordCount.from_dict(record_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


