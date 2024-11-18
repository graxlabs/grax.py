# SearchFieldFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name to filter. | [optional] 
**filter_type** | **str** | Filtering operator. &#39;eq&#39;, &#39;lt&#39;, &#39;lte&#39;, &#39;gt&#39;, &#39;gte&#39;, &#39;contains&#39;, &#39;prefix&#39;, or &#39;suffix&#39;. | [optional] 
**var_not** | **bool** | Negates the filter. | [optional] 
**value** | **str** | Value to filter. Empty values with &#39;eq&#39; operation only. | [optional] 

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
search_field_filter_from_dict = SearchFieldFilter.from_dict(search_field_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


