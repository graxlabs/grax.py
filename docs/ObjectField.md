# ObjectField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Field label. | [optional] 
**name** | **str** | Field name. | [optional] 
**name_field** | **bool** | Is name field. | [optional] 
**type** | **str** | Field type. | [optional] 

## Example

```python
from grax.models.object_field import ObjectField

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectField from a JSON string
object_field_instance = ObjectField.from_json(json)
# print the JSON string representation of the object
print(ObjectField.to_json())

# convert the object into a dict
object_field_dict = object_field_instance.to_dict()
# create an instance of ObjectField from a dict
object_field_from_dict = ObjectField.from_dict(object_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


