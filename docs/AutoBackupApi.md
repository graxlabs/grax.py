# grax.AutoBackupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backups_health_get**](AutoBackupApi.md#backups_health_get) | **GET** /api/v1/backups/health | Get Auto Backup health


# **backups_health_get**
> BackupsHealth backups_health_get(max_behind=max_behind)

Get Auto Backup health

Get the health of Auto Backup.

### Example

* Bearer (GRAX Token) Authentication (bearer_token):

```python
import grax
from grax.models.backups_health import BackupsHealth
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
    api_instance = grax.AutoBackupApi(api_client)
    max_behind = 56 # int | Maximum time behind before the backups are considered unhealthy, in seconds. (optional)

    try:
        # Get Auto Backup health
        api_response = api_instance.backups_health_get(max_behind=max_behind)
        print("The response of AutoBackupApi->backups_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoBackupApi->backups_health_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_behind** | **int**| Maximum time behind before the backups are considered unhealthy, in seconds. | [optional] 

### Return type

[**BackupsHealth**](BackupsHealth.md)

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

