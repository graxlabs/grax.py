# RecordsPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Token to retrieve the next page of results, blank if done. | [optional] 
**records** | [**List[Record]**](Record.md) | Records. | [optional] 

## Example

```python
from grax.models.records_page import RecordsPage

# TODO update the JSON string below
json = "{}"
# create an instance of RecordsPage from a JSON string
records_page_instance = RecordsPage.from_json(json)
# print the JSON string representation of the object
print(RecordsPage.to_json())

# convert the object into a dict
records_page_dict = records_page_instance.to_dict()
# create an instance of RecordsPage from a dict
records_page_form_dict = records_page.from_dict(records_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


