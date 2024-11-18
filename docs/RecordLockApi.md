# grax.RecordLockApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**record_lock**](RecordLockApi.md#record_lock) | **POST** /api/v1/salesforce/{orgID}/objects/{object}/records/{id}/lock | Lock single record
[**record_lock_get**](RecordLockApi.md#record_lock_get) | **GET** /api/v1/salesforce/{orgID}/objects/{object}/records/{id}/lock | Get record lock
[**record_unlock**](RecordLockApi.md#record_unlock) | **DELETE** /api/v1/salesforce/{orgID}/objects/{object}/records/{id}/lock | Unlock single record
[**records_lock**](RecordLockApi.md#records_lock) | **POST** /api/v1/salesforce/{orgID}/objects/{object}/lock | Lock multiple records
[**records_unlock**](RecordLockApi.md#records_unlock) | **POST** /api/v1/salesforce/{orgID}/objects/{object}/unlock | Unlock multiple records


# **record_lock**
> record_lock(org_id, object, id, lock_record_schema=lock_record_schema)

Lock single record

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.lock_record_schema import LockRecordSchema
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
    api_instance = grax.RecordLockApi(api_client)
    org_id = '00D000000000001AAA' # str | Organization ID. Can be 'fromAuth' to infer from authenticated user.
    object = 'Account' # str | Object name.
    id = '001000000000001AAA' # str | Record ID.
    lock_record_schema = grax.LockRecordSchema() # LockRecordSchema |  (optional)

    try:
        # Lock single record
        api_instance.record_lock(org_id, object, id, lock_record_schema=lock_record_schema)
    except Exception as e:
        print("Exception when calling RecordLockApi->record_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID. Can be &#39;fromAuth&#39; to infer from authenticated user. | 
 **object** | **str**| Object name. | 
 **id** | **str**| Record ID. | 
 **lock_record_schema** | [**LockRecordSchema**](LockRecordSchema.md)|  | [optional] 

### Return type

void (empty response body)

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

# **record_lock_get**
> RecordLock record_lock_get(org_id, object, id)

Get record lock

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.record_lock import RecordLock
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
    api_instance = grax.RecordLockApi(api_client)
    org_id = '00D000000000001AAA' # str | Organization ID. Can be 'fromAuth' to infer from authenticated user.
    object = 'Account' # str | Object name.
    id = '001000000000001AAA' # str | Record ID.

    try:
        # Get record lock
        api_response = api_instance.record_lock_get(org_id, object, id)
        print("The response of RecordLockApi->record_lock_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordLockApi->record_lock_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID. Can be &#39;fromAuth&#39; to infer from authenticated user. | 
 **object** | **str**| Object name. | 
 **id** | **str**| Record ID. | 

### Return type

[**RecordLock**](RecordLock.md)

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

# **record_unlock**
> record_unlock(org_id, object, id)

Unlock single record

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
    api_instance = grax.RecordLockApi(api_client)
    org_id = '00D000000000001AAA' # str | Organization ID. Can be 'fromAuth' to infer from authenticated user.
    object = 'Account' # str | Object name.
    id = '001000000000001AAA' # str | Record ID.

    try:
        # Unlock single record
        api_instance.record_unlock(org_id, object, id)
    except Exception as e:
        print("Exception when calling RecordLockApi->record_unlock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID. Can be &#39;fromAuth&#39; to infer from authenticated user. | 
 **object** | **str**| Object name. | 
 **id** | **str**| Record ID. | 

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
**200** | OK |  -  |
**4XX** | Error |  -  |
**5XX** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **records_lock**
> records_lock(org_id, object, lock_object_records_schema=lock_object_records_schema)

Lock multiple records

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.lock_object_records_schema import LockObjectRecordsSchema
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
    api_instance = grax.RecordLockApi(api_client)
    org_id = '00D000000000001AAA' # str | Organization ID. Can be 'fromAuth' to infer from authenticated user.
    object = 'Account' # str | Object name.
    lock_object_records_schema = {"ids":[{"id":"acc001","note":"Note on first lock"},{"id":"acc002"}]} # LockObjectRecordsSchema |  (optional)

    try:
        # Lock multiple records
        api_instance.records_lock(org_id, object, lock_object_records_schema=lock_object_records_schema)
    except Exception as e:
        print("Exception when calling RecordLockApi->records_lock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID. Can be &#39;fromAuth&#39; to infer from authenticated user. | 
 **object** | **str**| Object name. | 
 **lock_object_records_schema** | [**LockObjectRecordsSchema**](LockObjectRecordsSchema.md)|  | [optional] 

### Return type

void (empty response body)

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

# **records_unlock**
> records_unlock(org_id, object, unlock_object_records_schema=unlock_object_records_schema)

Unlock multiple records

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.unlock_object_records_schema import UnlockObjectRecordsSchema
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
    api_instance = grax.RecordLockApi(api_client)
    org_id = '00D000000000001AAA' # str | Organization ID. Can be 'fromAuth' to infer from authenticated user.
    object = 'Account' # str | Object name.
    unlock_object_records_schema = {"ids":["acc001","acc002"]} # UnlockObjectRecordsSchema |  (optional)

    try:
        # Unlock multiple records
        api_instance.records_unlock(org_id, object, unlock_object_records_schema=unlock_object_records_schema)
    except Exception as e:
        print("Exception when calling RecordLockApi->records_unlock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **str**| Organization ID. Can be &#39;fromAuth&#39; to infer from authenticated user. | 
 **object** | **str**| Object name. | 
 **unlock_object_records_schema** | [**UnlockObjectRecordsSchema**](UnlockObjectRecordsSchema.md)|  | [optional] 

### Return type

void (empty response body)

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

