# RecordCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | [**List[RecordCount]**](RecordCount.md) |  | [optional] 
**incomplete** | **bool** | Indicates when counts are still being backfilled. | [optional] 

## Example

```python
from grax.models.record_counts import RecordCounts

# TODO update the JSON string below
json = "{}"
# create an instance of RecordCounts from a JSON string
record_counts_instance = RecordCounts.from_json(json)
# print the JSON string representation of the object
print(RecordCounts.to_json())

# convert the object into a dict
record_counts_dict = record_counts_instance.to_dict()
# create an instance of RecordCounts from a dict
record_counts_from_dict = RecordCounts.from_dict(record_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


