# grax

Generated with:

```
openapi-generator generate -i grax.yaml -o . -g python --package-name grax --git-user-id graxlabs --git-repo-id grax.py
```


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Generator version: 7.4.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/graxlabs/grax.py.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/graxlabs/grax.py.git`)

Then import the package:
```python
import grax
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import grax
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = grax.AutoBackupApi(api_client)
    max_behind = 56 # int | Maximum time behind before the backups are considered unhealthy, in seconds. (optional)

    try:
        # Get Auto Backup health
        api_response = api_instance.backups_health_get(max_behind=max_behind)
        print("The response of AutoBackupApi->backups_health_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutoBackupApi->backups_health_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AutoBackupApi* | [**backups_health_get**](docs/AutoBackupApi.md#backups_health_get) | **GET** /api/v1/backups/health | Get Auto Backup health
*DeleteForeverApi* | [**deletion_get**](docs/DeleteForeverApi.md#deletion_get) | **GET** /api/v1/salesforce/{orgID}/deletions/{id} | Get Delete Forever deletion
*DeleteForeverApi* | [**deletion_records_list**](docs/DeleteForeverApi.md#deletion_records_list) | **GET** /api/v1/salesforce/{orgID}/deletions/{id}/records | List Delete Forever deletion records
*DeleteForeverApi* | [**deletions_list**](docs/DeleteForeverApi.md#deletions_list) | **GET** /api/v1/salesforce/{orgID}/deletions | List Delete Forever deletions
*ObjectsApi* | [**objects_list**](docs/ObjectsApi.md#objects_list) | **GET** /api/v2/objects | List objects
*RecordLockApi* | [**record_lock**](docs/RecordLockApi.md#record_lock) | **POST** /api/v1/salesforce/{orgID}/objects/{object}/records/{id}/lock | Lock single record
*RecordLockApi* | [**record_lock_get**](docs/RecordLockApi.md#record_lock_get) | **GET** /api/v1/salesforce/{orgID}/objects/{object}/records/{id}/lock | Get record lock
*RecordLockApi* | [**record_unlock**](docs/RecordLockApi.md#record_unlock) | **DELETE** /api/v1/salesforce/{orgID}/objects/{object}/records/{id}/lock | Unlock single record
*RecordLockApi* | [**records_lock**](docs/RecordLockApi.md#records_lock) | **POST** /api/v1/salesforce/{orgID}/objects/{object}/lock | Lock multiple records
*RecordLockApi* | [**records_unlock**](docs/RecordLockApi.md#records_unlock) | **POST** /api/v1/salesforce/{orgID}/objects/{object}/unlock | Unlock multiple records
*RecordsApi* | [**record_children_list**](docs/RecordsApi.md#record_children_list) | **GET** /api/v1/salesforce/{orgID}/objects/{object}/records/{id}/versions/{mod}/children | List record children
*RecordsApi* | [**record_get**](docs/RecordsApi.md#record_get) | **GET** /api/v2/objects/{object}/records/{id} | Get record
*RecordsApi* | [**record_versions_list**](docs/RecordsApi.md#record_versions_list) | **GET** /api/v2/objects/{object}/records/{id}/versions | List record versions
*RecordsApi* | [**records_list**](docs/RecordsApi.md#records_list) | **GET** /api/v2/objects/{object}/records | List records
*SearchApi* | [**search_abort**](docs/SearchApi.md#search_abort) | **POST** /api/v2/searches/{id}/abort | Abort search
*SearchApi* | [**search_create**](docs/SearchApi.md#search_create) | **POST** /api/v2/searches | Create search
*SearchApi* | [**search_delete**](docs/SearchApi.md#search_delete) | **DELETE** /api/v2/searches/{id} | Delete search
*SearchApi* | [**search_download**](docs/SearchApi.md#search_download) | **GET** /api/v2/searches/{id}/download | Download search results
*SearchApi* | [**search_get**](docs/SearchApi.md#search_get) | **GET** /api/v2/searches/{id} | Get search
*SearchApi* | [**search_records**](docs/SearchApi.md#search_records) | **GET** /api/v2/searches/{id}/records | Read search result records
*SearchApi* | [**searches_list**](docs/SearchApi.md#searches_list) | **GET** /api/v2/searches | List searches


## Documentation For Models

 - [AuditUser](docs/AuditUser.md)
 - [BackupsHealth](docs/BackupsHealth.md)
 - [ChildRecord](docs/ChildRecord.md)
 - [Deletion](docs/Deletion.md)
 - [DeletionCaller](docs/DeletionCaller.md)
 - [DeletionRecord](docs/DeletionRecord.md)
 - [DeletionRecordsPage](docs/DeletionRecordsPage.md)
 - [DeletionsPage](docs/DeletionsPage.md)
 - [Error](docs/Error.md)
 - [ErrorBody](docs/ErrorBody.md)
 - [Object](docs/Object.md)
 - [ObjectsPage](docs/ObjectsPage.md)
 - [Record](docs/Record.md)
 - [RecordChildrenPage](docs/RecordChildrenPage.md)
 - [RecordDeleted](docs/RecordDeleted.md)
 - [RecordField](docs/RecordField.md)
 - [RecordLock](docs/RecordLock.md)
 - [RecordLockID](docs/RecordLockID.md)
 - [RecordPurged](docs/RecordPurged.md)
 - [RecordRestoredFrom](docs/RecordRestoredFrom.md)
 - [RecordVersionsPage](docs/RecordVersionsPage.md)
 - [RecordsLockRequest](docs/RecordsLockRequest.md)
 - [RecordsPage](docs/RecordsPage.md)
 - [RecordsUnlockRequest](docs/RecordsUnlockRequest.md)
 - [Search](docs/Search.md)
 - [SearchCreate](docs/SearchCreate.md)
 - [SearchFieldFilter](docs/SearchFieldFilter.md)
 - [SearchFilters](docs/SearchFilters.md)
 - [SearchLimits](docs/SearchLimits.md)
 - [SearchRecord](docs/SearchRecord.md)
 - [SearchRecordsPage](docs/SearchRecordsPage.md)
 - [SearchesPage](docs/SearchesPage.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearer_token"></a>
### bearer_token

- **Type**: Bearer authentication (GRAX Token)


## Author




