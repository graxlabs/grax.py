# AuditUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email. | [optional] 
**id** | **str** | User ID. | [optional] 
**name** | **str** | User name. | [optional] 

## Example

```python
from grax.models.audit_user import AuditUser

# TODO update the JSON string below
json = "{}"
# create an instance of AuditUser from a JSON string
audit_user_instance = AuditUser.from_json(json)
# print the JSON string representation of the object
print(AuditUser.to_json())

# convert the object into a dict
audit_user_dict = audit_user_instance.to_dict()
# create an instance of AuditUser from a dict
audit_user_from_dict = AuditUser.from_dict(audit_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


