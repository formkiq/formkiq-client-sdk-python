# formkiq_client.SystemManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_api_key**](SystemManagementApi.md#add_api_key) | **POST** /sites/{siteId}/apiKeys | Add API Key
[**add_locale**](SystemManagementApi.md#add_locale) | **POST** /sites/{siteId}/locales | Add Locale
[**add_locale_resource_item**](SystemManagementApi.md#add_locale_resource_item) | **POST** /sites/{siteId}/locales/{locale}/resourceItems | Add Locale Resource Item
[**add_open_search_restore_snapshot**](SystemManagementApi.md#add_open_search_restore_snapshot) | **POST** /sites/{siteId}/opensearch/snapshots/{snapshotName}/restore | Restore site OpenSearch snapshot
[**add_open_search_snapshot**](SystemManagementApi.md#add_open_search_snapshot) | **POST** /sites/{siteId}/opensearch/snapshots/{snapshotName} | Create site OpenSearch snapshot
[**add_site**](SystemManagementApi.md#add_site) | **POST** /sites | Add Site
[**add_system_inference_model_agreement**](SystemManagementApi.md#add_system_inference_model_agreement) | **POST** /system/inferenceModels/agreement | Agree to a system inference model
[**cleanup_open_search_snapshot_repository**](SystemManagementApi.md#cleanup_open_search_snapshot_repository) | **POST** /sites/global/opensearch/snapshotRepositories/{repositoryName}/cleanup | Cleanup OpenSearch snapshot repository
[**delete_api_key**](SystemManagementApi.md#delete_api_key) | **DELETE** /sites/{siteId}/apiKeys/{apiKey} | Delete API Key
[**delete_locale**](SystemManagementApi.md#delete_locale) | **DELETE** /sites/{siteId}/locales/{locale} | Delete Locale
[**delete_locale_resource_item**](SystemManagementApi.md#delete_locale_resource_item) | **DELETE** /sites/{siteId}/locales/{locale}/resourceItems/{itemKey} | Delete Local Resource Item
[**delete_open_search_index**](SystemManagementApi.md#delete_open_search_index) | **DELETE** /sites/{siteId}/opensearch/index | Deletes site(s) OpenSearch index
[**delete_open_search_index_by_name**](SystemManagementApi.md#delete_open_search_index_by_name) | **DELETE** /sites/global/opensearch/indices/{indexName} | Deletes OpenSearch index by name
[**delete_open_search_restore_snapshot**](SystemManagementApi.md#delete_open_search_restore_snapshot) | **DELETE** /sites/{siteId}/opensearch/snapshots/{snapshotName}/restore | Delete restored OpenSearch snapshot index
[**delete_open_search_snapshot**](SystemManagementApi.md#delete_open_search_snapshot) | **DELETE** /sites/{siteId}/opensearch/snapshots/{snapshotName} | Delete site OpenSearch snapshot
[**delete_open_search_snapshot_repository**](SystemManagementApi.md#delete_open_search_snapshot_repository) | **DELETE** /sites/{siteId}/opensearch/snapshotRepository | Delete site OpenSearch snapshot repository
[**delete_site_group**](SystemManagementApi.md#delete_site_group) | **DELETE** /sites/{siteId}/groups/{groupName} | Deletes Site Group and permissions
[**generate_delegation_token**](SystemManagementApi.md#generate_delegation_token) | **POST** /sites/{siteId}/delegationTokens | Generate a delegation token
[**get_all_open_search_indices**](SystemManagementApi.md#get_all_open_search_indices) | **GET** /sites/global/opensearch/indices | Get all OpenSearch indices
[**get_api_keys**](SystemManagementApi.md#get_api_keys) | **GET** /sites/{siteId}/apiKeys | Get API Keys
[**get_configuration**](SystemManagementApi.md#get_configuration) | **GET** /sites/{siteId}/configuration | Get site configuration
[**get_locale_resource_item**](SystemManagementApi.md#get_locale_resource_item) | **GET** /sites/{siteId}/locales/{locale}/resourceItems/{itemKey} | Get Resource Item by Locale
[**get_locale_resource_items**](SystemManagementApi.md#get_locale_resource_items) | **GET** /sites/{siteId}/locales/{locale}/resourceItems | Get Resource Items by Locale
[**get_locales**](SystemManagementApi.md#get_locales) | **GET** /sites/{siteId}/locales | Get Locales
[**get_open_search_index**](SystemManagementApi.md#get_open_search_index) | **GET** /sites/{siteId}/opensearch/index | Get site(s) OpenSearch index settings
[**get_open_search_indices**](SystemManagementApi.md#get_open_search_indices) | **GET** /sites/{siteId}/opensearch/indices | Get site(s) OpenSearch indices
[**get_open_search_snapshot**](SystemManagementApi.md#get_open_search_snapshot) | **GET** /sites/{siteId}/opensearch/snapshots/{snapshotName} | Get site OpenSearch snapshot
[**get_open_search_snapshot_repositories**](SystemManagementApi.md#get_open_search_snapshot_repositories) | **GET** /sites/global/opensearch/snapshotRepositories | List OpenSearch snapshot repositories
[**get_open_search_snapshot_repository**](SystemManagementApi.md#get_open_search_snapshot_repository) | **GET** /sites/{siteId}/opensearch/snapshotRepository | Get site OpenSearch snapshot repository
[**get_open_search_snapshots**](SystemManagementApi.md#get_open_search_snapshots) | **GET** /sites/{siteId}/opensearch/snapshots | List site OpenSearch snapshots
[**get_site_group**](SystemManagementApi.md#get_site_group) | **GET** /sites/{siteId}/groups/{groupName} | Get group and permissions belonging to site
[**get_site_groups**](SystemManagementApi.md#get_site_groups) | **GET** /sites/{siteId}/groups | Get group(s) and permissions belonging to site
[**get_sites**](SystemManagementApi.md#get_sites) | **GET** /sites | Get site(s) access
[**get_system_configuration**](SystemManagementApi.md#get_system_configuration) | **GET** /system/configuration | Get system configuration
[**get_system_inference_models**](SystemManagementApi.md#get_system_inference_models) | **GET** /system/inferenceModels | Get system inference models
[**get_version**](SystemManagementApi.md#get_version) | **GET** /version | Get FormKiQ version
[**set_locale_resource_item**](SystemManagementApi.md#set_locale_resource_item) | **PUT** /sites/{siteId}/locales/{locale}/resourceItems/{itemKey} | Set Locale Resource Item
[**set_open_search_index**](SystemManagementApi.md#set_open_search_index) | **PUT** /sites/{siteId}/opensearch/index | Set site(s) OpenSearch index settings
[**set_open_search_indices**](SystemManagementApi.md#set_open_search_indices) | **PUT** /sites/{siteId}/opensearch/indices | Set site(s) OpenSearch index to use for a SiteId
[**set_site_group_permissions**](SystemManagementApi.md#set_site_group_permissions) | **PUT** /sites/{siteId}/groups/{groupName}/permissions | Set Site&#39;s Group Permissions
[**update_configuration**](SystemManagementApi.md#update_configuration) | **PATCH** /sites/{siteId}/configuration | Update site configuration
[**update_site**](SystemManagementApi.md#update_site) | **PATCH** /sites/{siteId} | Update Site
[**update_system_configuration**](SystemManagementApi.md#update_system_configuration) | **PATCH** /system/configuration | Update system configuration


# **add_api_key**
> AddApiKeyResponse add_api_key(site_id, add_api_key_request)

Add API Key

Adds a new API Key

### Example


```python
import formkiq_client
from formkiq_client.models.add_api_key_request import AddApiKeyRequest
from formkiq_client.models.add_api_key_response import AddApiKeyResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    add_api_key_request = {"name":"My API Key"} # AddApiKeyRequest | 

    try:
        # Add API Key
        api_response = api_instance.add_api_key(site_id, add_api_key_request)
        print("The response of SystemManagementApi->add_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->add_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **add_api_key_request** | [**AddApiKeyRequest**](AddApiKeyRequest.md)|  | 

### Return type

[**AddApiKeyResponse**](AddApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_locale**
> AddResponse add_locale(site_id, add_locale_request)

Add Locale

Adds a new locale to the specified site

### Example


```python
import formkiq_client
from formkiq_client.models.add_locale_request import AddLocaleRequest
from formkiq_client.models.add_response import AddResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    add_locale_request = formkiq_client.AddLocaleRequest() # AddLocaleRequest | 

    try:
        # Add Locale
        api_response = api_instance.add_locale(site_id, add_locale_request)
        print("The response of SystemManagementApi->add_locale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->add_locale: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **add_locale_request** | [**AddLocaleRequest**](AddLocaleRequest.md)|  | 

### Return type

[**AddResponse**](AddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_locale_resource_item**
> AddLocaleResourceItemResponse add_locale_resource_item(site_id, locale, add_locale_resource_item_request)

Add Locale Resource Item

Adds a new localized resource item for a given locale

### Example


```python
import formkiq_client
from formkiq_client.models.add_locale_resource_item_request import AddLocaleResourceItemRequest
from formkiq_client.models.add_locale_resource_item_response import AddLocaleResourceItemResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    locale = 'locale_example' # str | Site Locale (ISO 639 / ISO 3166)
    add_locale_resource_item_request = {"resourceItem":{"itemType":"INTERFACE","interfaceKey":"mainMenuTitle","localizedValue":"Main Menu"}} # AddLocaleResourceItemRequest | 

    try:
        # Add Locale Resource Item
        api_response = api_instance.add_locale_resource_item(site_id, locale, add_locale_resource_item_request)
        print("The response of SystemManagementApi->add_locale_resource_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->add_locale_resource_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **locale** | **str**| Site Locale (ISO 639 / ISO 3166) | 
 **add_locale_resource_item_request** | [**AddLocaleResourceItemRequest**](AddLocaleResourceItemRequest.md)|  | 

### Return type

[**AddLocaleResourceItemResponse**](AddLocaleResourceItemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 201 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_open_search_restore_snapshot**
> AddResponse add_open_search_restore_snapshot(site_id, snapshot_name)

Restore site OpenSearch snapshot

Restores the specified snapshot into a separate OpenSearch index for the site.

The restored index is created from the site's current index name with the snapshot name and "_restored" suffix. For provisioned OpenSearch domains, the snapshot is read from the site's S3 snapshot repository. For OpenSearch Serverless, the snapshot is read from the automated snapshot repository.

### Example


```python
import formkiq_client
from formkiq_client.models.add_response import AddResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    snapshot_name = 'snapshot_name_example' # str | Snapshot Name

    try:
        # Restore site OpenSearch snapshot
        api_response = api_instance.add_open_search_restore_snapshot(site_id, snapshot_name)
        print("The response of SystemManagementApi->add_open_search_restore_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->add_open_search_restore_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **snapshot_name** | **str**| Snapshot Name | 

### Return type

[**AddResponse**](AddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_open_search_snapshot**
> AddResponse add_open_search_snapshot(site_id, snapshot_name)

Create site OpenSearch snapshot

Creates a manual snapshot of the specified site's OpenSearch index.

If the site's S3 snapshot repository does not already exist, it is registered before the snapshot is created. The supplied snapshot name is stored with the site prefix. This operation is not supported for OpenSearch Serverless.

### Example


```python
import formkiq_client
from formkiq_client.models.add_response import AddResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    snapshot_name = 'snapshot_name_example' # str | Snapshot Name

    try:
        # Create site OpenSearch snapshot
        api_response = api_instance.add_open_search_snapshot(site_id, snapshot_name)
        print("The response of SystemManagementApi->add_open_search_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->add_open_search_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **snapshot_name** | **str**| Snapshot Name | 

### Return type

[**AddResponse**](AddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_site**
> AddResponse add_site(add_site_request)

Add Site

Add Site

### Example


```python
import formkiq_client
from formkiq_client.models.add_response import AddResponse
from formkiq_client.models.add_site_request import AddSiteRequest
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    add_site_request = formkiq_client.AddSiteRequest() # AddSiteRequest | 

    try:
        # Add Site
        api_response = api_instance.add_site(add_site_request)
        print("The response of SystemManagementApi->add_site:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->add_site: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_site_request** | [**AddSiteRequest**](AddSiteRequest.md)|  | 

### Return type

[**AddResponse**](AddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_system_inference_model_agreement**
> AddResponse add_system_inference_model_agreement(add_system_inference_model_agreement_request)

Agree to a system inference model

Agree to the Bedrock model usage agreement for a system inference model

### Example


```python
import formkiq_client
from formkiq_client.models.add_response import AddResponse
from formkiq_client.models.add_system_inference_model_agreement_request import AddSystemInferenceModelAgreementRequest
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    add_system_inference_model_agreement_request = formkiq_client.AddSystemInferenceModelAgreementRequest() # AddSystemInferenceModelAgreementRequest | 

    try:
        # Agree to a system inference model
        api_response = api_instance.add_system_inference_model_agreement(add_system_inference_model_agreement_request)
        print("The response of SystemManagementApi->add_system_inference_model_agreement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->add_system_inference_model_agreement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_system_inference_model_agreement_request** | [**AddSystemInferenceModelAgreementRequest**](AddSystemInferenceModelAgreementRequest.md)|  | 

### Return type

[**AddResponse**](AddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cleanup_open_search_snapshot_repository**
> CleanupOpenSearchSnapshotRepositoryResponse cleanup_open_search_snapshot_repository(repository_name, cluster_manager_timeout=cluster_manager_timeout, timeout=timeout)

Cleanup OpenSearch snapshot repository

Cleans up stale data in the specified OpenSearch snapshot repository.

This endpoint clears data no longer referenced by any existing snapshot. This operation is not supported for OpenSearch Serverless.

### Example


```python
import formkiq_client
from formkiq_client.models.cleanup_open_search_snapshot_repository_response import CleanupOpenSearchSnapshotRepositoryResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    repository_name = 'repository_name_example' # str | Snapshot Repository Name
    cluster_manager_timeout = 'cluster_manager_timeout_example' # str | The amount of time to wait for a response from the cluster manager node. (optional)
    timeout = 'timeout_example' # str | The amount of time to wait for the operation to complete. (optional)

    try:
        # Cleanup OpenSearch snapshot repository
        api_response = api_instance.cleanup_open_search_snapshot_repository(repository_name, cluster_manager_timeout=cluster_manager_timeout, timeout=timeout)
        print("The response of SystemManagementApi->cleanup_open_search_snapshot_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->cleanup_open_search_snapshot_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Snapshot Repository Name | 
 **cluster_manager_timeout** | **str**| The amount of time to wait for a response from the cluster manager node. | [optional] 
 **timeout** | **str**| The amount of time to wait for the operation to complete. | [optional] 

### Return type

[**CleanupOpenSearchSnapshotRepositoryResponse**](CleanupOpenSearchSnapshotRepositoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> DeleteApiKeyResponse delete_api_key(site_id, api_key)

Delete API Key

Adds a new API Key

### Example


```python
import formkiq_client
from formkiq_client.models.delete_api_key_response import DeleteApiKeyResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    api_key = 'api_key_example' # str | API Key

    try:
        # Delete API Key
        api_response = api_instance.delete_api_key(site_id, api_key)
        print("The response of SystemManagementApi->delete_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **api_key** | **str**| API Key | 

### Return type

[**DeleteApiKeyResponse**](DeleteApiKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_locale**
> DeleteResponse delete_locale(site_id, locale)

Delete Locale

Delete Locale

### Example


```python
import formkiq_client
from formkiq_client.models.delete_response import DeleteResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    locale = 'locale_example' # str | Site Locale (ISO 639 / ISO 3166)

    try:
        # Delete Locale
        api_response = api_instance.delete_locale(site_id, locale)
        print("The response of SystemManagementApi->delete_locale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->delete_locale: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **locale** | **str**| Site Locale (ISO 639 / ISO 3166) | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_locale_resource_item**
> DeleteResponse delete_locale_resource_item(site_id, locale, item_key)

Delete Local Resource Item

Delete Local Resource Item

### Example


```python
import formkiq_client
from formkiq_client.models.delete_response import DeleteResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    locale = 'locale_example' # str | Site Locale (ISO 639 / ISO 3166)
    item_key = 'item_key_example' # str | Item Key (MUST be URL‑encoded)

    try:
        # Delete Local Resource Item
        api_response = api_instance.delete_locale_resource_item(site_id, locale, item_key)
        print("The response of SystemManagementApi->delete_locale_resource_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->delete_locale_resource_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **locale** | **str**| Site Locale (ISO 639 / ISO 3166) | 
 **item_key** | **str**| Item Key (MUST be URL‑encoded) | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_open_search_index**
> DeleteResponse delete_open_search_index(site_id)

Deletes site(s) OpenSearch index

Deletes the OpenSearch index

### Example


```python
import formkiq_client
from formkiq_client.models.delete_response import DeleteResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Deletes site(s) OpenSearch index
        api_response = api_instance.delete_open_search_index(site_id)
        print("The response of SystemManagementApi->delete_open_search_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->delete_open_search_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_open_search_index_by_name**
> DeleteResponse delete_open_search_index_by_name(index_name)

Deletes OpenSearch index by name

Deletes the OpenSearch index by name

### Example


```python
import formkiq_client
from formkiq_client.models.delete_response import DeleteResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    index_name = 'index_name_example' # str | IndexName to path

    try:
        # Deletes OpenSearch index by name
        api_response = api_instance.delete_open_search_index_by_name(index_name)
        print("The response of SystemManagementApi->delete_open_search_index_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->delete_open_search_index_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_name** | **str**| IndexName to path | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_open_search_restore_snapshot**
> DeleteResponse delete_open_search_restore_snapshot(site_id, snapshot_name)

Delete restored OpenSearch snapshot index

Deletes the restored OpenSearch index created from the specified snapshot.

This deletes only the restored index named with the snapshot name and "_restored" suffix. It does not delete the original site index or the snapshot. This operation is not supported for OpenSearch Serverless.

### Example


```python
import formkiq_client
from formkiq_client.models.delete_response import DeleteResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    snapshot_name = 'snapshot_name_example' # str | Snapshot Name

    try:
        # Delete restored OpenSearch snapshot index
        api_response = api_instance.delete_open_search_restore_snapshot(site_id, snapshot_name)
        print("The response of SystemManagementApi->delete_open_search_restore_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->delete_open_search_restore_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **snapshot_name** | **str**| Snapshot Name | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_open_search_snapshot**
> DeleteResponse delete_open_search_snapshot(site_id, snapshot_name)

Delete site OpenSearch snapshot

Deletes a manual snapshot from the specified site's S3 snapshot repository.

The supplied snapshot name is resolved to the site's stored snapshot name before deletion. This operation is not supported for OpenSearch Serverless.

### Example


```python
import formkiq_client
from formkiq_client.models.delete_response import DeleteResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    snapshot_name = 'snapshot_name_example' # str | Snapshot Name

    try:
        # Delete site OpenSearch snapshot
        api_response = api_instance.delete_open_search_snapshot(site_id, snapshot_name)
        print("The response of SystemManagementApi->delete_open_search_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->delete_open_search_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **snapshot_name** | **str**| Snapshot Name | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_open_search_snapshot_repository**
> DeleteResponse delete_open_search_snapshot_repository(site_id)

Delete site OpenSearch snapshot repository

Deletes the S3 snapshot repository configured for the specified site's OpenSearch index.

This removes the OpenSearch repository registration, not the site's index. This operation is not supported for OpenSearch Serverless.

### Example


```python
import formkiq_client
from formkiq_client.models.delete_response import DeleteResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Delete site OpenSearch snapshot repository
        api_response = api_instance.delete_open_search_snapshot_repository(site_id)
        print("The response of SystemManagementApi->delete_open_search_snapshot_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->delete_open_search_snapshot_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_group**
> DeleteResponse delete_site_group(site_id, group_name)

Deletes Site Group and permissions

Deletes Site Group and permissions

### Example


```python
import formkiq_client
from formkiq_client.models.delete_response import DeleteResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    group_name = 'group_name_example' # str | Group Name

    try:
        # Deletes Site Group and permissions
        api_response = api_instance.delete_site_group(site_id, group_name)
        print("The response of SystemManagementApi->delete_site_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->delete_site_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **group_name** | **str**| Group Name | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_delegation_token**
> AddDelegationTokenResponse generate_delegation_token(site_id, add_delegation_token_request)

Generate a delegation token

Creates a KMS-signed delegation token for a site. This endpoint requires ADMIN permission
for the requested siteId. The returned token is sent on later API requests in the
x-formkiq-delegation-token header and reduces the caller's effective permissions to the
requested subset for that site. It cannot grant ADMIN, add permissions the caller does not
already have, or add access to other sites. When onBehalfOf is supplied, activity created
while using the token is attributed to that username while the signed token still records
the ADMIN principal that issued it. The reason is signed into the token for audit and
support traceability.

### Example


```python
import formkiq_client
from formkiq_client.models.add_delegation_token_request import AddDelegationTokenRequest
from formkiq_client.models.add_delegation_token_response import AddDelegationTokenResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    add_delegation_token_request = formkiq_client.AddDelegationTokenRequest() # AddDelegationTokenRequest | 

    try:
        # Generate a delegation token
        api_response = api_instance.generate_delegation_token(site_id, add_delegation_token_request)
        print("The response of SystemManagementApi->generate_delegation_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->generate_delegation_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **add_delegation_token_request** | [**AddDelegationTokenRequest**](AddDelegationTokenRequest.md)|  | 

### Return type

[**AddDelegationTokenResponse**](AddDelegationTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_open_search_indices**
> GetOpenSearchIndiceResponse get_all_open_search_indices()

Get all OpenSearch indices

Returns all OpenSearch indices

### Example


```python
import formkiq_client
from formkiq_client.models.get_open_search_indice_response import GetOpenSearchIndiceResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)

    try:
        # Get all OpenSearch indices
        api_response = api_instance.get_all_open_search_indices()
        print("The response of SystemManagementApi->get_all_open_search_indices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_all_open_search_indices: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOpenSearchIndiceResponse**](GetOpenSearchIndiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_keys**
> GetApiKeysResponse get_api_keys(site_id, next=next, limit=limit)

Get API Keys

Returns the list of ApiKeys

### Example


```python
import formkiq_client
from formkiq_client.models.get_api_keys_response import GetApiKeysResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get API Keys
        api_response = api_instance.get_api_keys(site_id, next=next, limit=limit)
        print("The response of SystemManagementApi->get_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetApiKeysResponse**](GetApiKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration**
> GetConfigurationResponse get_configuration(site_id)

Get site configuration

Returns the list of sites that the user has access to

### Example


```python
import formkiq_client
from formkiq_client.models.get_configuration_response import GetConfigurationResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Get site configuration
        api_response = api_instance.get_configuration(site_id)
        print("The response of SystemManagementApi->get_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**GetConfigurationResponse**](GetConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locale_resource_item**
> GetLocaleResourceItemResponse get_locale_resource_item(site_id, locale, item_key)

Get Resource Item by Locale

Returns the resource item

### Example


```python
import formkiq_client
from formkiq_client.models.get_locale_resource_item_response import GetLocaleResourceItemResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    locale = 'locale_example' # str | Site Locale (ISO 639 / ISO 3166)
    item_key = 'item_key_example' # str | Item Key (MUST be URL‑encoded)

    try:
        # Get Resource Item by Locale
        api_response = api_instance.get_locale_resource_item(site_id, locale, item_key)
        print("The response of SystemManagementApi->get_locale_resource_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_locale_resource_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **locale** | **str**| Site Locale (ISO 639 / ISO 3166) | 
 **item_key** | **str**| Item Key (MUST be URL‑encoded) | 

### Return type

[**GetLocaleResourceItemResponse**](GetLocaleResourceItemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locale_resource_items**
> GetLocaleResourceItemsResponse get_locale_resource_items(site_id, locale, next=next, limit=limit)

Get Resource Items by Locale

Returns the list resource items

### Example


```python
import formkiq_client
from formkiq_client.models.get_locale_resource_items_response import GetLocaleResourceItemsResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    locale = 'locale_example' # str | Site Locale (ISO 639 / ISO 3166)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get Resource Items by Locale
        api_response = api_instance.get_locale_resource_items(site_id, locale, next=next, limit=limit)
        print("The response of SystemManagementApi->get_locale_resource_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_locale_resource_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **locale** | **str**| Site Locale (ISO 639 / ISO 3166) | 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetLocaleResourceItemsResponse**](GetLocaleResourceItemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locales**
> GetLocalesResponse get_locales(site_id, next=next, limit=limit)

Get Locales

Returns a list of locale(s) in a specified site

### Example


```python
import formkiq_client
from formkiq_client.models.get_locales_response import GetLocalesResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get Locales
        api_response = api_instance.get_locales(site_id, next=next, limit=limit)
        print("The response of SystemManagementApi->get_locales:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_locales: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetLocalesResponse**](GetLocalesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_search_index**
> GetOpenSearchIndexResponse get_open_search_index(site_id)

Get site(s) OpenSearch index settings

Returns the OpenSearch index settings 

(Deprecated use /sites/{siteId}/opensearch/indices)

### Example


```python
import formkiq_client
from formkiq_client.models.get_open_search_index_response import GetOpenSearchIndexResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Get site(s) OpenSearch index settings
        api_response = api_instance.get_open_search_index(site_id)
        print("The response of SystemManagementApi->get_open_search_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_open_search_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**GetOpenSearchIndexResponse**](GetOpenSearchIndexResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_search_indices**
> GetOpenSearchIndiceResponse get_open_search_indices(site_id)

Get site(s) OpenSearch indices

Returns the OpenSearch indices

### Example


```python
import formkiq_client
from formkiq_client.models.get_open_search_indice_response import GetOpenSearchIndiceResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Get site(s) OpenSearch indices
        api_response = api_instance.get_open_search_indices(site_id)
        print("The response of SystemManagementApi->get_open_search_indices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_open_search_indices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**GetOpenSearchIndiceResponse**](GetOpenSearchIndiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_search_snapshot**
> GetOpenSearchSnapshotResponse get_open_search_snapshot(site_id, snapshot_name)

Get site OpenSearch snapshot

Returns details for a snapshot of the specified site's OpenSearch index.

For provisioned OpenSearch domains, the supplied snapshot name is resolved to the site's stored snapshot name before lookup. For OpenSearch Serverless, the response is read from the automated snapshot repository.

### Example


```python
import formkiq_client
from formkiq_client.models.get_open_search_snapshot_response import GetOpenSearchSnapshotResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    snapshot_name = 'snapshot_name_example' # str | Snapshot Name

    try:
        # Get site OpenSearch snapshot
        api_response = api_instance.get_open_search_snapshot(site_id, snapshot_name)
        print("The response of SystemManagementApi->get_open_search_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_open_search_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **snapshot_name** | **str**| Snapshot Name | 

### Return type

[**GetOpenSearchSnapshotResponse**](GetOpenSearchSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_search_snapshot_repositories**
> GetOpenSearchSnapshotRepositoryResponse get_open_search_snapshot_repositories()

List OpenSearch snapshot repositories

Returns all configured OpenSearch S3 snapshot repositories for the deployment.

This endpoint is available to administrators when the fulltext OpenSearch module is installed and snapshot support is enabled. Snapshot repositories are not supported for OpenSearch Serverless.

### Example


```python
import formkiq_client
from formkiq_client.models.get_open_search_snapshot_repository_response import GetOpenSearchSnapshotRepositoryResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)

    try:
        # List OpenSearch snapshot repositories
        api_response = api_instance.get_open_search_snapshot_repositories()
        print("The response of SystemManagementApi->get_open_search_snapshot_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_open_search_snapshot_repositories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOpenSearchSnapshotRepositoryResponse**](GetOpenSearchSnapshotRepositoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_search_snapshot_repository**
> GetOpenSearchSnapshotRepositoryResponse get_open_search_snapshot_repository(site_id)

Get site OpenSearch snapshot repository

Returns the S3 snapshot repository configured for the specified site.

The repository stores manual snapshots for the site's OpenSearch index. It is named from the site and application environment and is created automatically when a snapshot is requested. Snapshot repositories are not supported for OpenSearch Serverless.

### Example


```python
import formkiq_client
from formkiq_client.models.get_open_search_snapshot_repository_response import GetOpenSearchSnapshotRepositoryResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Get site OpenSearch snapshot repository
        api_response = api_instance.get_open_search_snapshot_repository(site_id)
        print("The response of SystemManagementApi->get_open_search_snapshot_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_open_search_snapshot_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**GetOpenSearchSnapshotRepositoryResponse**](GetOpenSearchSnapshotRepositoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_open_search_snapshots**
> GetOpenSearchSnapshotResponse get_open_search_snapshots(site_id)

List site OpenSearch snapshots

Returns snapshots for the specified site's OpenSearch index.

For provisioned OpenSearch domains, the response is read from the site's S3 snapshot repository. For OpenSearch Serverless, the response is read from the automated snapshot repository.

### Example


```python
import formkiq_client
from formkiq_client.models.get_open_search_snapshot_response import GetOpenSearchSnapshotResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # List site OpenSearch snapshots
        api_response = api_instance.get_open_search_snapshots(site_id)
        print("The response of SystemManagementApi->get_open_search_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_open_search_snapshots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**GetOpenSearchSnapshotResponse**](GetOpenSearchSnapshotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_group**
> GetSiteGroupResponse get_site_group(site_id, group_name)

Get group and permissions belonging to site

Returns details of a group and permissions belonging to site

### Example


```python
import formkiq_client
from formkiq_client.models.get_site_group_response import GetSiteGroupResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    group_name = 'group_name_example' # str | Group Name

    try:
        # Get group and permissions belonging to site
        api_response = api_instance.get_site_group(site_id, group_name)
        print("The response of SystemManagementApi->get_site_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_site_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **group_name** | **str**| Group Name | 

### Return type

[**GetSiteGroupResponse**](GetSiteGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_groups**
> GetSiteGroupsResponse get_site_groups(site_id)

Get group(s) and permissions belonging to site

Returns list of groups and permissions belonging to site

### Example


```python
import formkiq_client
from formkiq_client.models.get_site_groups_response import GetSiteGroupsResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Get group(s) and permissions belonging to site
        api_response = api_instance.get_site_groups(site_id)
        print("The response of SystemManagementApi->get_site_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_site_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**GetSiteGroupsResponse**](GetSiteGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sites**
> GetSitesResponse get_sites(status=status)

Get site(s) access

Returns the list of sites that the user has access to

### Example


```python
import formkiq_client
from formkiq_client.models.get_sites_response import GetSitesResponse
from formkiq_client.models.site_status import SiteStatus
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    status = formkiq_client.SiteStatus() # SiteStatus | Fetch sites with status (only valid when using SitePermissions 'defined' (optional)

    try:
        # Get site(s) access
        api_response = api_instance.get_sites(status=status)
        print("The response of SystemManagementApi->get_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_sites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**SiteStatus**](.md)| Fetch sites with status (only valid when using SitePermissions &#39;defined&#39; | [optional] 

### Return type

[**GetSitesResponse**](GetSitesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_configuration**
> GetSystemConfigurationResponse get_system_configuration()

Get system configuration

Returns the system configuration

### Example


```python
import formkiq_client
from formkiq_client.models.get_system_configuration_response import GetSystemConfigurationResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)

    try:
        # Get system configuration
        api_response = api_instance.get_system_configuration()
        print("The response of SystemManagementApi->get_system_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_system_configuration: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSystemConfigurationResponse**](GetSystemConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_inference_models**
> GetSystemInferenceModelsResponse get_system_inference_models()

Get system inference models

Returns the system inference models

### Example


```python
import formkiq_client
from formkiq_client.models.get_system_inference_models_response import GetSystemInferenceModelsResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)

    try:
        # Get system inference models
        api_response = api_instance.get_system_inference_models()
        print("The response of SystemManagementApi->get_system_inference_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_system_inference_models: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSystemInferenceModelsResponse**](GetSystemInferenceModelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> GetVersionResponse get_version()

Get FormKiQ version

Return the version of FormKiQ

### Example


```python
import formkiq_client
from formkiq_client.models.get_version_response import GetVersionResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)

    try:
        # Get FormKiQ version
        api_response = api_instance.get_version()
        print("The response of SystemManagementApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetVersionResponse**](GetVersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_locale_resource_item**
> SetResponse set_locale_resource_item(site_id, locale, item_key, set_locale_resource_item_request)

Set Locale Resource Item

Set a new Locale Resource Item

### Example


```python
import formkiq_client
from formkiq_client.models.set_locale_resource_item_request import SetLocaleResourceItemRequest
from formkiq_client.models.set_response import SetResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    locale = 'locale_example' # str | Site Locale (ISO 639 / ISO 3166)
    item_key = 'item_key_example' # str | Item Key (MUST be URL‑encoded)
    set_locale_resource_item_request = formkiq_client.SetLocaleResourceItemRequest() # SetLocaleResourceItemRequest | 

    try:
        # Set Locale Resource Item
        api_response = api_instance.set_locale_resource_item(site_id, locale, item_key, set_locale_resource_item_request)
        print("The response of SystemManagementApi->set_locale_resource_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->set_locale_resource_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **locale** | **str**| Site Locale (ISO 639 / ISO 3166) | 
 **item_key** | **str**| Item Key (MUST be URL‑encoded) | 
 **set_locale_resource_item_request** | [**SetLocaleResourceItemRequest**](SetLocaleResourceItemRequest.md)|  | 

### Return type

[**SetResponse**](SetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_open_search_index**
> SetOpenSearchIndexResponse set_open_search_index(site_id, set_open_search_index_request)

Set site(s) OpenSearch index settings

Sets the OpenSearch index settings

### Example


```python
import formkiq_client
from formkiq_client.models.set_open_search_index_request import SetOpenSearchIndexRequest
from formkiq_client.models.set_open_search_index_response import SetOpenSearchIndexResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    set_open_search_index_request = formkiq_client.SetOpenSearchIndexRequest() # SetOpenSearchIndexRequest | 

    try:
        # Set site(s) OpenSearch index settings
        api_response = api_instance.set_open_search_index(site_id, set_open_search_index_request)
        print("The response of SystemManagementApi->set_open_search_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->set_open_search_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **set_open_search_index_request** | [**SetOpenSearchIndexRequest**](SetOpenSearchIndexRequest.md)|  | 

### Return type

[**SetOpenSearchIndexResponse**](SetOpenSearchIndexResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_open_search_indices**
> SetResponse set_open_search_indices(site_id, set_open_search_indice_request)

Set site(s) OpenSearch index to use for a SiteId

Sets the OpenSearch index to use for a SiteId

### Example


```python
import formkiq_client
from formkiq_client.models.set_open_search_indice_request import SetOpenSearchIndiceRequest
from formkiq_client.models.set_response import SetResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    set_open_search_indice_request = formkiq_client.SetOpenSearchIndiceRequest() # SetOpenSearchIndiceRequest | 

    try:
        # Set site(s) OpenSearch index to use for a SiteId
        api_response = api_instance.set_open_search_indices(site_id, set_open_search_indice_request)
        print("The response of SystemManagementApi->set_open_search_indices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->set_open_search_indices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **set_open_search_indice_request** | [**SetOpenSearchIndiceRequest**](SetOpenSearchIndiceRequest.md)|  | 

### Return type

[**SetResponse**](SetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_site_group_permissions**
> SetResponse set_site_group_permissions(site_id, group_name, set_group_permissions_request)

Set Site's Group Permissions

Set Site's Group Permissions

### Example


```python
import formkiq_client
from formkiq_client.models.set_group_permissions_request import SetGroupPermissionsRequest
from formkiq_client.models.set_response import SetResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    group_name = 'group_name_example' # str | Group Name
    set_group_permissions_request = formkiq_client.SetGroupPermissionsRequest() # SetGroupPermissionsRequest | 

    try:
        # Set Site's Group Permissions
        api_response = api_instance.set_site_group_permissions(site_id, group_name, set_group_permissions_request)
        print("The response of SystemManagementApi->set_site_group_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->set_site_group_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **group_name** | **str**| Group Name | 
 **set_group_permissions_request** | [**SetGroupPermissionsRequest**](SetGroupPermissionsRequest.md)|  | 

### Return type

[**SetResponse**](SetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration**
> UpdateConfigurationResponse update_configuration(site_id, update_configuration_request)

Update site configuration

Update the System Management configuration

### Example


```python
import formkiq_client
from formkiq_client.models.update_configuration_request import UpdateConfigurationRequest
from formkiq_client.models.update_configuration_response import UpdateConfigurationResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    update_configuration_request = formkiq_client.UpdateConfigurationRequest() # UpdateConfigurationRequest | 

    try:
        # Update site configuration
        api_response = api_instance.update_configuration(site_id, update_configuration_request)
        print("The response of SystemManagementApi->update_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->update_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **update_configuration_request** | [**UpdateConfigurationRequest**](UpdateConfigurationRequest.md)|  | 

### Return type

[**UpdateConfigurationResponse**](UpdateConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site**
> UpdateResponse update_site(site_id, update_site_request)

Update Site

Update Site

### Example


```python
import formkiq_client
from formkiq_client.models.update_response import UpdateResponse
from formkiq_client.models.update_site_request import UpdateSiteRequest
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    update_site_request = formkiq_client.UpdateSiteRequest() # UpdateSiteRequest | 

    try:
        # Update Site
        api_response = api_instance.update_site(site_id, update_site_request)
        print("The response of SystemManagementApi->update_site:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->update_site: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **update_site_request** | [**UpdateSiteRequest**](UpdateSiteRequest.md)|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_system_configuration**
> UpdateResponse update_system_configuration(update_system_configuration_request)

Update system configuration

Update the system configuration

### Example


```python
import formkiq_client
from formkiq_client.models.update_response import UpdateResponse
from formkiq_client.models.update_system_configuration_request import UpdateSystemConfigurationRequest
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.SystemManagementApi(api_client)
    update_system_configuration_request = formkiq_client.UpdateSystemConfigurationRequest() # UpdateSystemConfigurationRequest | 

    try:
        # Update system configuration
        api_response = api_instance.update_system_configuration(update_system_configuration_request)
        print("The response of SystemManagementApi->update_system_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->update_system_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_system_configuration_request** | [**UpdateSystemConfigurationRequest**](UpdateSystemConfigurationRequest.md)|  | 

### Return type

[**UpdateResponse**](UpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

