# grax.RecordsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**record_children_list**](RecordsApi.md#record_children_list) | **GET** /api/v1/salesforce/{orgID}/objects/{object}/records/{id}/versions/{mod}/children | List record children
[**record_counts_get**](RecordsApi.md#record_counts_get) | **GET** /api/v2/record-counts | Get estimated record counts
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
    org_id = '00D000000000001AAA' # str | Organization ID. Can be 'fromAuth' to infer from authenticated user.
    object2 = 'Account' # str | Object name.
    id = '001000000000001AAA' # str | Record ID.
    mod = 'mod_example' # str | Unused.
    object = 'object_example' # str | Child object to list. (optional)
    fields = 'fields_example' # str | Fields to include in the response. Can be 'all' for all fields, 'name' for the name field, or a comma separated list of field names. (optional)
    delete_source = 'delete_source_example' # str | Delete source to filter by, can be 'any', 'grax' or 'salesforce'. (optional)
    page_size = 56 # int | Maximum number of results to return per page. Fewer or zero may be returned. (optional)
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
 **org_id** | **str**| Organization ID. Can be &#39;fromAuth&#39; to infer from authenticated user. | 
 **object2** | **str**| Object name. | 
 **id** | **str**| Record ID. | 
 **mod** | **str**| Unused. | 
 **object** | **str**| Child object to list. | [optional] 
 **fields** | **str**| Fields to include in the response. Can be &#39;all&#39; for all fields, &#39;name&#39; for the name field, or a comma separated list of field names. | [optional] 
 **delete_source** | **str**| Delete source to filter by, can be &#39;any&#39;, &#39;grax&#39; or &#39;salesforce&#39;. | [optional] 
 **page_size** | **int**| Maximum number of results to return per page. Fewer or zero may be returned. | [optional] 
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

# **record_counts_get**
> RecordCounts record_counts_get(object=object, min=min, max=max, group=group)

Get estimated record counts

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.record_counts import RecordCounts
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
    object = 'Account' # str | Object to return counts for. Can be 'all' to break out counts by object. If not specified, counts are summed across all objects. (optional)
    min = '2024-01-01T00:00Z' # datetime | Minimum time, inclusive. Must be supplied with 'group'. (optional)
    max = '2024-01-01T00:00Z' # datetime | Maximum time, inclusive. Must be supplied with 'group'. (optional)
    group = 'group_example' # str | Time group to bucket counts: 'hour', 'day', 'month' and 'year'. Defaults to all time, which cannot be used with min/max. (optional)

    try:
        # Get estimated record counts
        api_response = api_instance.record_counts_get(object=object, min=min, max=max, group=group)
        print("The response of RecordsApi->record_counts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsApi->record_counts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object to return counts for. Can be &#39;all&#39; to break out counts by object. If not specified, counts are summed across all objects. | [optional] 
 **min** | **datetime**| Minimum time, inclusive. Must be supplied with &#39;group&#39;. | [optional] 
 **max** | **datetime**| Maximum time, inclusive. Must be supplied with &#39;group&#39;. | [optional] 
 **group** | **str**| Time group to bucket counts: &#39;hour&#39;, &#39;day&#39;, &#39;month&#39; and &#39;year&#39;. Defaults to all time, which cannot be used with min/max. | [optional] 

### Return type

[**RecordCounts**](RecordCounts.md)

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
    object = 'Account' # str | Object name, or '_infer' if you want GRAX to do a lookup based on record ID.
    id = '001000000000001AAA' # str | Record ID.
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
 **object** | **str**| Object name, or &#39;_infer&#39; if you want GRAX to do a lookup based on record ID. | 
 **id** | **str**| Record ID. | 
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
    object = 'Account' # str | Object name.
    id = '001000000000001AAA' # str | Record ID.
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
 **id** | **str**| Record ID. | 
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
    object = 'Account' # str | Object name.
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

