# RecordField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Field name. | [optional] 
**value** | **str** | Field value. | [optional] 

## Example

```python
from grax.models.record_field import RecordField

# TODO update the JSON string below
json = "{}"
# create an instance of RecordField from a JSON string
record_field_instance = RecordField.from_json(json)
# print the JSON string representation of the object
print(RecordField.to_json())

# convert the object into a dict
record_field_dict = record_field_instance.to_dict()
# create an instance of RecordField from a dict
record_field_form_dict = record_field.from_dict(record_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


