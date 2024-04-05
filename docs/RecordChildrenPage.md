# RecordChildrenPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_page_token** | **str** | Token to retrieve the next page of results, blank if done. | [optional] 
**records** | [**List[ChildRecord]**](ChildRecord.md) |  | [optional] 

## Example

```python
from grax.models.record_children_page import RecordChildrenPage

# TODO update the JSON string below
json = "{}"
# create an instance of RecordChildrenPage from a JSON string
record_children_page_instance = RecordChildrenPage.from_json(json)
# print the JSON string representation of the object
print(RecordChildrenPage.to_json())

# convert the object into a dict
record_children_page_dict = record_children_page_instance.to_dict()
# create an instance of RecordChildrenPage from a dict
record_children_page_form_dict = record_children_page.from_dict(record_children_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


