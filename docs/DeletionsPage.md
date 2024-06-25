# DeletionsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deletions** | [**List[Deletion]**](Deletion.md) |  | [optional] 
**next_page_token** | **str** | Token to retrieve the next page of results, blank if done. | [optional] 

## Example

```python
from grax.models.deletions_page import DeletionsPage

# TODO update the JSON string below
json = "{}"
# create an instance of DeletionsPage from a JSON string
deletions_page_instance = DeletionsPage.from_json(json)
# print the JSON string representation of the object
print(DeletionsPage.to_json())

# convert the object into a dict
deletions_page_dict = deletions_page_instance.to_dict()
# create an instance of DeletionsPage from a dict
deletions_page_from_dict = DeletionsPage.from_dict(deletions_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


