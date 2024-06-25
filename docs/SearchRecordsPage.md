# SearchRecordsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_continue_page_token** | **str** | Token to retrieve the next page of running search results. | [optional] 
**next_page_token** | **str** | Token to retrieve the next page of results, blank if done. | [optional] 
**records** | [**List[SearchRecord]**](SearchRecord.md) |  | [optional] 

## Example

```python
from grax.models.search_records_page import SearchRecordsPage

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRecordsPage from a JSON string
search_records_page_instance = SearchRecordsPage.from_json(json)
# print the JSON string representation of the object
print(SearchRecordsPage.to_json())

# convert the object into a dict
search_records_page_dict = search_records_page_instance.to_dict()
# create an instance of SearchRecordsPage from a dict
search_records_page_from_dict = SearchRecordsPage.from_dict(search_records_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


