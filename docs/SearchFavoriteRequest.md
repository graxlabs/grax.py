# SearchFavoriteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite** | **bool** | Favorite status of the search. | [optional] 

## Example

```python
from grax.models.search_favorite_request import SearchFavoriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFavoriteRequest from a JSON string
search_favorite_request_instance = SearchFavoriteRequest.from_json(json)
# print the JSON string representation of the object
print(SearchFavoriteRequest.to_json())

# convert the object into a dict
search_favorite_request_dict = search_favorite_request_instance.to_dict()
# create an instance of SearchFavoriteRequest from a dict
search_favorite_request_from_dict = SearchFavoriteRequest.from_dict(search_favorite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


