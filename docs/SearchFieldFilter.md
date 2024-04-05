# SearchFieldFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** |  | [optional] 
**filter_type** | **str** |  | [optional] 
**var_not** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from grax.models.search_field_filter import SearchFieldFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFieldFilter from a JSON string
search_field_filter_instance = SearchFieldFilter.from_json(json)
# print the JSON string representation of the object
print(SearchFieldFilter.to_json())

# convert the object into a dict
search_field_filter_dict = search_field_filter_instance.to_dict()
# create an instance of SearchFieldFilter from a dict
search_field_filter_form_dict = search_field_filter.from_dict(search_field_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


