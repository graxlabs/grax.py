# ObjectFieldsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[ObjectField]**](ObjectField.md) | Fields. | [optional] 
**next_page_token** | **str** | Token to retrieve the next page of results, blank if done. | [optional] 

## Example

```python
from grax.models.object_fields_page import ObjectFieldsPage

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectFieldsPage from a JSON string
object_fields_page_instance = ObjectFieldsPage.from_json(json)
# print the JSON string representation of the object
print(ObjectFieldsPage.to_json())

# convert the object into a dict
object_fields_page_dict = object_fields_page_instance.to_dict()
# create an instance of ObjectFieldsPage from a dict
object_fields_page_from_dict = ObjectFieldsPage.from_dict(object_fields_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


