# grax.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_abort**](SearchApi.md#search_abort) | **POST** /api/v2/searches/{id}/abort | Abort search
[**search_create**](SearchApi.md#search_create) | **POST** /api/v2/searches | Create search
[**search_delete**](SearchApi.md#search_delete) | **DELETE** /api/v2/searches/{id} | Delete search
[**search_download**](SearchApi.md#search_download) | **GET** /api/v2/searches/{id}/download | Download search results
[**search_get**](SearchApi.md#search_get) | **GET** /api/v2/searches/{id} | Get search
[**search_records**](SearchApi.md#search_records) | **GET** /api/v2/searches/{id}/records | Read search result records
[**searches_list**](SearchApi.md#searches_list) | **GET** /api/v2/searches | List searches


# **search_abort**
> search_abort(id)

Abort search

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
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
    api_instance = grax.SearchApi(api_client)
    id = 'id_example' # str | ID of the search job.

    try:
        # Abort search
        api_instance.search_abort(id)
    except Exception as e:
        print("Exception when calling SearchApi->search_abort: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the search job. | 

### Return type

void (empty response body)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_create**
> Search search_create(search_create=search_create)

Create search

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.search import Search
from grax.models.search_create import SearchCreate
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
    api_instance = grax.SearchApi(api_client)
    search_create = grax.SearchCreate() # SearchCreate |  (optional)

    try:
        # Create search
        api_response = api_instance.search_create(search_create=search_create)
        print("The response of SearchApi->search_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_create** | [**SearchCreate**](SearchCreate.md)|  | [optional] 

### Return type

[**Search**](Search.md)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_delete**
> search_delete(id)

Delete search

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
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
    api_instance = grax.SearchApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete search
        api_instance.search_delete(id)
    except Exception as e:
        print("Exception when calling SearchApi->search_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_download**
> bytearray search_download(id, fields=fields, latest=latest)

Download search results

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
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
    api_instance = grax.SearchApi(api_client)
    id = 'id_example' # str | ID of the search job.
    fields = 'fields_example' # str | Fields to include in the response. If not specified, all fields are included. (optional)
    latest = True # bool | Whether to download the latest version of each record. (optional)

    try:
        # Download search results
        api_response = api_instance.search_download(id, fields=fields, latest=latest)
        print("The response of SearchApi->search_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the search job. | 
 **fields** | **str**| Fields to include in the response. If not specified, all fields are included. | [optional] 
 **latest** | **bool**| Whether to download the latest version of each record. | [optional] 

### Return type

**bytearray**

### Authorization

[bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_get**
> Search search_get(id)

Get search

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.search import Search
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
    api_instance = grax.SearchApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get search
        api_response = api_instance.search_get(id)
        print("The response of SearchApi->search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Search**](Search.md)

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

# **search_records**
> SearchRecordsPage search_records(id, fields=fields, reverse=reverse, min_time=min_time, max_items=max_items, page_token=page_token)

Read search result records

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.search_records_page import SearchRecordsPage
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
    api_instance = grax.SearchApi(api_client)
    id = 'id_example' # str | ID of the search job.
    fields = 'fields_example' # str | Fields to include in the response. Can be 'all' for all fields, 'name' for the name field, or a comma separated list of field names. (optional)
    reverse = True # bool | Search records in reverse order. (optional)
    min_time = '2013-10-20T19:20:30+01:00' # datetime | Minimum record time to include in the response. (optional)
    max_items = 56 # int | Maximum number of items to return per page. Fewer or zero may be returned. (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page. (optional)

    try:
        # Read search result records
        api_response = api_instance.search_records(id, fields=fields, reverse=reverse, min_time=min_time, max_items=max_items, page_token=page_token)
        print("The response of SearchApi->search_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->search_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the search job. | 
 **fields** | **str**| Fields to include in the response. Can be &#39;all&#39; for all fields, &#39;name&#39; for the name field, or a comma separated list of field names. | [optional] 
 **reverse** | **bool**| Search records in reverse order. | [optional] 
 **min_time** | **datetime**| Minimum record time to include in the response. | [optional] 
 **max_items** | **int**| Maximum number of items to return per page. Fewer or zero may be returned. | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page. | [optional] 

### Return type

[**SearchRecordsPage**](SearchRecordsPage.md)

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

# **searches_list**
> SearchesPage searches_list(max_items=max_items, page_token=page_token)

List searches

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.searches_page import SearchesPage
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
    api_instance = grax.SearchApi(api_client)
    max_items = 56 # int | Maximum number of items to return per page. Fewer or zero may be returned. (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page. (optional)

    try:
        # List searches
        api_response = api_instance.searches_list(max_items=max_items, page_token=page_token)
        print("The response of SearchApi->searches_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->searches_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_items** | **int**| Maximum number of items to return per page. Fewer or zero may be returned. | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page. | [optional] 

### Return type

[**SearchesPage**](SearchesPage.md)

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

