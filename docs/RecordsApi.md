# grax.RecordsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**record_children_list**](RecordsApi.md#record_children_list) | **GET** /api/v1/salesforce/{orgID}/objects/{object}/records/{id}/versions/{mod}/children | List record children
[**record_get**](RecordsApi.md#record_get) | **GET** /api/v2/objects/{object}/records/{id} | Get record
[**record_versions_list**](RecordsApi.md#record_versions_list) | **GET** /api/v2/objects/{object}/records/{id}/versions | List record versions
[**records_list**](RecordsApi.md#records_list) | **GET** /api/v2/objects/{object}/records | List records


# **record_children_list**
> RecordChildrenPage record_children_list(org_id, object2, id, mod, object=object, fields=fields, delete_source=delete_source, page_size=page_size, page_token=page_token)

List record children

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.record_children_page import RecordChildrenPage
from grax.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = grax.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (GRAX Token): bearer_token
configuration = grax.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with grax.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grax.RecordsApi(api_client)
    org_id = 'org_id_example' # str | 
    object2 = 'object_example' # str | 
    id = 'id_example' # str | 
    mod = 'mod_example' # str | 
    object = 'object_example' # str | The child object to list. (optional)
    fields = 'fields_example' # str | The fields to include in the response. Can be 'all' for all fields, 'name' for the name field, or a comma separated list of field names. (optional)
    delete_source = 'delete_source_example' # str | The delete source to filter by, can be 'any', 'grax' or 'salesforce'. (optional)
    page_size = 56 # int | Maximum number of results to return per page. (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page. (optional)

    try:
        # List record children
        api_response = api_instance.record_children_list(org_id, object2, id, mod, object=object, fields=fields, delete_source=delete_source, page_size=page_size, page_token=page_token)
        print("The response of RecordsApi->record_children_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->record_children_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **object2** | **str**|  | 
 **id** | **str**|  | 
 **mod** | **str**|  | 
 **object** | **str**| The child object to list. | [optional] 
 **fields** | **str**| The fields to include in the response. Can be &#39;all&#39; for all fields, &#39;name&#39; for the name field, or a comma separated list of field names. | [optional] 
 **delete_source** | **str**| The delete source to filter by, can be &#39;any&#39;, &#39;grax&#39; or &#39;salesforce&#39;. | [optional] 
 **page_size** | **int**| Maximum number of results to return per page. | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page. | [optional] 

### Return type

[**RecordChildrenPage**](RecordChildrenPage.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_get**
> Record record_get(object, id, fields=fields)

Get record

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.record import Record
from grax.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = grax.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (GRAX Token): bearer_token
configuration = grax.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with grax.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grax.RecordsApi(api_client)
    object = 'object_example' # str | Object name.
    id = 'id_example' # str | ID of the record.
    fields = 'fields_example' # str | Fields to include in the response. Can be 'all' for all fields, 'name' for the name field, or a comma separated list of field names. (optional)

    try:
        # Get record
        api_response = api_instance.record_get(object, id, fields=fields)
        print("The response of RecordsApi->record_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->record_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object name. | 
 **id** | **str**| ID of the record. | 
 **fields** | **str**| Fields to include in the response. Can be &#39;all&#39; for all fields, &#39;name&#39; for the name field, or a comma separated list of field names. | [optional] 

### Return type

[**Record**](Record.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_versions_list**
> RecordVersionsPage record_versions_list(object, id, fields=fields, max_items=max_items, page_token=page_token)

List record versions

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.record_versions_page import RecordVersionsPage
from grax.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = grax.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (GRAX Token): bearer_token
configuration = grax.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with grax.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grax.RecordsApi(api_client)
    object = 'object_example' # str | Object name.
    id = 'id_example' # str | ID of the record.
    fields = 'fields_example' # str | Fields to include in the response. Can be 'all' for all fields, 'name' for the name field, or a comma separated list of field names. (optional)
    max_items = 56 # int | Maximum number of items to return per page. Fewer or zero may be returned. (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page. (optional)

    try:
        # List record versions
        api_response = api_instance.record_versions_list(object, id, fields=fields, max_items=max_items, page_token=page_token)
        print("The response of RecordsApi->record_versions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->record_versions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object name. | 
 **id** | **str**| ID of the record. | 
 **fields** | **str**| Fields to include in the response. Can be &#39;all&#39; for all fields, &#39;name&#39; for the name field, or a comma separated list of field names. | [optional] 
 **max_items** | **int**| Maximum number of items to return per page. Fewer or zero may be returned. | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page. | [optional] 

### Return type

[**RecordVersionsPage**](RecordVersionsPage.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **records_list**
> RecordsPage records_list(object, fields=fields, max_items=max_items, page_token=page_token)

List records

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.records_page import RecordsPage
from grax.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = grax.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (GRAX Token): bearer_token
configuration = grax.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with grax.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = grax.RecordsApi(api_client)
    object = 'object_example' # str | Object name.
    fields = 'fields_example' # str | Fields to include in the response. Can be 'all' for all fields, 'name' for the name field, or a comma separated list of field names. (optional)
    max_items = 56 # int | Maximum number of items to return per page. Fewer or zero may be returned. (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page. (optional)

    try:
        # List records
        api_response = api_instance.records_list(object, fields=fields, max_items=max_items, page_token=page_token)
        print("The response of RecordsApi->records_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->records_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object name. | 
 **fields** | **str**| Fields to include in the response. Can be &#39;all&#39; for all fields, &#39;name&#39; for the name field, or a comma separated list of field names. | [optional] 
 **max_items** | **int**| Maximum number of items to return per page. Fewer or zero may be returned. | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page. | [optional] 

### Return type

[**RecordsPage**](RecordsPage.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

