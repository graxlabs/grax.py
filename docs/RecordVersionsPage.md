# RecordVersionsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Token to retrieve the next page of results, blank if done. | [optional] 
**records** | [**List[Record]**](Record.md) | Record versions. | [optional] 

## Example

```python
from grax.models.record_versions_page import RecordVersionsPage

# TODO update the JSON string below
json = "{}"
# create an instance of RecordVersionsPage from a JSON string
record_versions_page_instance = RecordVersionsPage.from_json(json)
# print the JSON string representation of the object
print(RecordVersionsPage.to_json())

# convert the object into a dict
record_versions_page_dict = record_versions_page_instance.to_dict()
# create an instance of RecordVersionsPage from a dict
record_versions_page_from_dict = RecordVersionsPage.from_dict(record_versions_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


