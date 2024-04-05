# grax.DeleteForeverApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletion_get**](DeleteForeverApi.md#deletion_get) | **GET** /api/v1/salesforce/{orgID}/deletions/{id} | Get Delete Forever deletion
[**deletion_records_list**](DeleteForeverApi.md#deletion_records_list) | **GET** /api/v1/salesforce/{orgID}/deletions/{id}/records | List Delete Forever deletion records
[**deletions_list**](DeleteForeverApi.md#deletions_list) | **GET** /api/v1/salesforce/{orgID}/deletions | List Delete Forever deletions


# **deletion_get**
> Deletion deletion_get(org_id, id)

Get Delete Forever deletion

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.deletion import Deletion
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
    api_instance = grax.DeleteForeverApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Get Delete Forever deletion
        api_response = api_instance.deletion_get(org_id, id)
        print("The response of DeleteForeverApi->deletion_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeleteForeverApi->deletion_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**Deletion**](Deletion.md)

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

# **deletion_records_list**
> DeletionRecordsPage deletion_records_list(org_id, id, page_size=page_size, page_token=page_token)

List Delete Forever deletion records

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.deletion_records_page import DeletionRecordsPage
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
    api_instance = grax.DeleteForeverApi(api_client)
    org_id = 'org_id_example' # str | 
    id = 'id_example' # str | 
    page_size = 56 # int | Maximum number of results to return per page. (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page. (optional)

    try:
        # List Delete Forever deletion records
        api_response = api_instance.deletion_records_list(org_id, id, page_size=page_size, page_token=page_token)
        print("The response of DeleteForeverApi->deletion_records_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeleteForeverApi->deletion_records_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **id** | **str**|  | 
 **page_size** | **int**| Maximum number of results to return per page. | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page. | [optional] 

### Return type

[**DeletionRecordsPage**](DeletionRecordsPage.md)

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

# **deletions_list**
> DeletionsPage deletions_list(org_id, min=min, max=max, object=object, page_size=page_size, page_token=page_token)

List Delete Forever deletions

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.deletions_page import DeletionsPage
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
    api_instance = grax.DeleteForeverApi(api_client)
    org_id = 'org_id_example' # str | 
    min = '2013-10-20T19:20:30+01:00' # datetime | Minimum created time, inclusive. (optional)
    max = '2013-10-20T19:20:30+01:00' # datetime | Maximum created time, exclusive. (optional)
    object = 'object_example' # str | Object name. If provided, only deletions for this object will be returned. (optional)
    page_size = 56 # int | Maximum number of results to return per page. (optional)
    page_token = 'page_token_example' # str | Token returned by previous call to retrieve the subsequent page. (optional)

    try:
        # List Delete Forever deletions
        api_response = api_instance.deletions_list(org_id, min=min, max=max, object=object, page_size=page_size, page_token=page_token)
        print("The response of DeleteForeverApi->deletions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeleteForeverApi->deletions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**|  | 
 **min** | **datetime**| Minimum created time, inclusive. | [optional] 
 **max** | **datetime**| Maximum created time, exclusive. | [optional] 
 **object** | **str**| Object name. If provided, only deletions for this object will be returned. | [optional] 
 **page_size** | **int**| Maximum number of results to return per page. | [optional] 
 **page_token** | **str**| Token returned by previous call to retrieve the subsequent page. | [optional] 

### Return type

[**DeletionsPage**](DeletionsPage.md)

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

