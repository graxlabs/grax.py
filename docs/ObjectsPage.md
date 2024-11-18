# ObjectsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Token to retrieve the next page of results, blank if done. | [optional] 
**objects** | [**List[Object]**](Object.md) | Objects. | [optional] 

## Example

```python
from grax.models.objects_page import ObjectsPage

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectsPage from a JSON string
objects_page_instance = ObjectsPage.from_json(json)
# print the JSON string representation of the object
print(ObjectsPage.to_json())

# convert the object into a dict
objects_page_dict = objects_page_instance.to_dict()
# create an instance of ObjectsPage from a dict
objects_page_from_dict = ObjectsPage.from_dict(objects_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


