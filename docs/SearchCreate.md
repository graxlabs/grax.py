# SearchCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**SearchFilters**](SearchFilters.md) |  | [optional] 
**limits** | [**SearchLimits**](SearchLimits.md) |  | [optional] 
**notify** | **bool** | Whether to notify when the search is complete. | [optional] 
**object** | **str** | Object to search. | [optional] 
**reverse** | **bool** | Whether to search in reverse order. | [optional] 
**status** | **str** | Status of the records to search. | [optional] 
**time_field** | **str** | Time field to search. Can be &#39;createdAt&#39;, &#39;modifiedAt&#39;, &#39;latestModifiedAt&#39;, &#39;rangeLatestModifiedAt&#39;, &#39;allModifiedAt&#39;, &#39;deletedAt&#39; or &#39;purgedAt&#39;. Defaults to &#39;createdAt&#39;. | [optional] 
**time_field_max** | **datetime** | Maximum time for the search. | [optional] 
**time_field_min** | **datetime** | Minimum time for the search. | [optional] 

## Example

```python
from grax.models.search_create import SearchCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SearchCreate from a JSON string
search_create_instance = SearchCreate.from_json(json)
# print the JSON string representation of the object
print(SearchCreate.to_json())

# convert the object into a dict
search_create_dict = search_create_instance.to_dict()
# create an instance of SearchCreate from a dict
search_create_form_dict = search_create.from_dict(search_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


