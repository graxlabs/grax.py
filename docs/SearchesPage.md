# SearchesPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Token to retrieve the next page of results, blank if done. | [optional] 
**searches** | [**List[Search]**](Search.md) |  | [optional] 

## Example

```python
from grax.models.searches_page import SearchesPage

# TODO update the JSON string below
json = "{}"
# create an instance of SearchesPage from a JSON string
searches_page_instance = SearchesPage.from_json(json)
# print the JSON string representation of the object
print(SearchesPage.to_json())

# convert the object into a dict
searches_page_dict = searches_page_instance.to_dict()
# create an instance of SearchesPage from a dict
searches_page_from_dict = SearchesPage.from_dict(searches_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


