# SearchLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **int** | Stop search after this many results are found. Limited to 10 million. | [optional] 

## Example

```python
from grax.models.search_limits import SearchLimits

# TODO update the JSON string below
json = "{}"
# create an instance of SearchLimits from a JSON string
search_limits_instance = SearchLimits.from_json(json)
# print the JSON string representation of the object
print(SearchLimits.to_json())

# convert the object into a dict
search_limits_dict = search_limits_instance.to_dict()
# create an instance of SearchLimits from a dict
search_limits_from_dict = SearchLimits.from_dict(search_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


