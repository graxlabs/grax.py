# SearchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[SearchFilters]**](SearchFilters.md) | Child filters. | [optional] 
**fields** | [**List[SearchFieldFilter]**](SearchFieldFilter.md) | Field filters. | [optional] 
**mode** | **str** | Mode of the filter. &#39;and&#39; requires all child and field filters match, &#39;or&#39; only requires one. | [optional] 

## Example

```python
from grax.models.search_filters import SearchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFilters from a JSON string
search_filters_instance = SearchFilters.from_json(json)
# print the JSON string representation of the object
print(SearchFilters.to_json())

# convert the object into a dict
search_filters_dict = search_filters_instance.to_dict()
# create an instance of SearchFilters from a dict
search_filters_from_dict = SearchFilters.from_dict(search_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


