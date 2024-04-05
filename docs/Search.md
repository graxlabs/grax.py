# Search


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Time the search job was created. | [optional] 
**deleting** | **datetime** | Time the search will be automatically deleted if its results are not accessed. | [optional] 
**filter_status** | **str** | Status of the records to search. | [optional] 
**filters** | [**SearchFilters**](SearchFilters.md) |  | [optional] 
**id** | **str** | ID of the search job. | [optional] 
**limits** | [**SearchLimits**](SearchLimits.md) |  | [optional] 
**name** | **str** | Name of the search job. | [optional] 
**object** | **str** | Object searched. | [optional] 
**progress** | **float** | Progress of the search job. | [optional] 
**records_found** | **int** | Number of records found. | [optional] 
**records_scanned** | **int** | Number of records scanned. | [optional] 
**records_time_first** | **datetime** | Time of the first found record. | [optional] 
**records_time_last** | **datetime** | Time of the last found record. | [optional] 
**reverse** | **bool** | Whether records were searched in reverse order. | [optional] 
**status** | **str** | Status of the search job. | [optional] 
**time_field** | **str** | Time field used for the search. Can be &#39;createdAt&#39;, &#39;modifiedAt&#39;, &#39;latestModifiedAt&#39;, &#39;rangeLatestModifiedAt&#39;, &#39;allModifiedAt&#39;, &#39;deletedAt&#39; or &#39;purgedAt&#39;. | [optional] 
**time_field_max** | **datetime** | Maximum time for the search. | [optional] 
**time_field_min** | **datetime** | Minimum time for the search. | [optional] 
**updated** | **datetime** | Time the search job was last updated. | [optional] 

## Example

```python
from grax.models.search import Search

# TODO update the JSON string below
json = "{}"
# create an instance of Search from a JSON string
search_instance = Search.from_json(json)
# print the JSON string representation of the object
print(Search.to_json())

# convert the object into a dict
search_dict = search_instance.to_dict()
# create an instance of Search from a dict
search_form_dict = search.from_dict(search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


