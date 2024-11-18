# grax.ObjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**object_fields_list**](ObjectsApi.md#object_fields_list) | **GET** /api/v2/objects/{object}/fields | List object fields
[**object_get**](ObjectsApi.md#object_get) | **GET** /api/v2/objects/{object} | Get object
[**objects_list**](ObjectsApi.md#objects_list) | **GET** /api/v2/objects | List objects


# **object_fields_list**
> ObjectFieldsPage object_fields_list(object, operation=operation, max_items=max_items, page_token=page_token)

List object fields

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.object_fields_page import ObjectFieldsPage
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
    api_instance = grax.ObjectsApi(api_client)
    object = 'Account' # str | Object name.
    operation = 'operation_example' # str | Operation type. Can be 'create', 'update', or 'upsert'. (optional)
    max_items = 56 # int | Maximum number of items to return per page. Fewer or zero may be returned. (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page. (optional)

    try:
        # List object fields
        api_response = api_instance.object_fields_list(object, operation=operation, max_items=max_items, page_token=page_token)
        print("The response of ObjectsApi->object_fields_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->object_fields_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object name. | 
 **operation** | **str**| Operation type. Can be &#39;create&#39;, &#39;update&#39;, or &#39;upsert&#39;. | [optional] 
 **max_items** | **int**| Maximum number of items to return per page. Fewer or zero may be returned. | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page. | [optional] 

### Return type

[**ObjectFieldsPage**](ObjectFieldsPage.md)

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

# **object_get**
> Object object_get(object)

Get object

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.object import Object
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
    api_instance = grax.ObjectsApi(api_client)
    object = 'Account' # str | Object name.

    try:
        # Get object
        api_response = api_instance.object_get(object)
        print("The response of ObjectsApi->object_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->object_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object** | **str**| Object name. | 

### Return type

[**Object**](Object.md)

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

# **objects_list**
> ObjectsPage objects_list(max_items=max_items, page_token=page_token)

List objects

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.objects_page import ObjectsPage
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
    api_instance = grax.ObjectsApi(api_client)
    max_items = 56 # int | Maximum number of items to return per page. Fewer or zero may be returned. (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page. (optional)

    try:
        # List objects
        api_response = api_instance.objects_list(max_items=max_items, page_token=page_token)
        print("The response of ObjectsApi->objects_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObjectsApi->objects_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_items** | **int**| Maximum number of items to return per page. Fewer or zero may be returned. | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page. | [optional] 

### Return type

[**ObjectsPage**](ObjectsPage.md)

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

