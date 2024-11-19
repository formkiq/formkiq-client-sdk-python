# formkiq_client.SystemManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_api_key**](SystemManagementApi.md#add_api_key) | **POST** /sites/{siteId}/apiKeys | Add API Key
[**add_site**](SystemManagementApi.md#add_site) | **POST** /sites | Add Site
[**delete_api_key**](SystemManagementApi.md#delete_api_key) | **DELETE** /sites/{siteId}/apiKeys/{apiKey} | Delete API Key
[**delete_opensearch_index**](SystemManagementApi.md#delete_opensearch_index) | **DELETE** /sites/{siteId}/opensearch/index | Deletes site(s) OpenSearch index
[**delete_site_group**](SystemManagementApi.md#delete_site_group) | **DELETE** /sites/{siteId}/groups/{groupName} | Deletes Site Group and permissions
[**get_api_keys**](SystemManagementApi.md#get_api_keys) | **GET** /sites/{siteId}/apiKeys | Get API Keys
[**get_configuration**](SystemManagementApi.md#get_configuration) | **GET** /sites/{siteId}/configuration | Get site configuration
[**get_opensearch_index**](SystemManagementApi.md#get_opensearch_index) | **GET** /sites/{siteId}/opensearch/index | Get site(s) OpenSearch index settings
[**get_site_group**](SystemManagementApi.md#get_site_group) | **GET** /sites/{siteId}/groups/{groupName} | Get group and permissions belonging to site
[**get_site_groups**](SystemManagementApi.md#get_site_groups) | **GET** /sites/{siteId}/groups | Get group(s) and permissions belonging to site
[**get_sites**](SystemManagementApi.md#get_sites) | **GET** /sites | Get site(s) access
[**get_version**](SystemManagementApi.md#get_version) | **GET** /version | Get FormKiQ version
[**set_opensearch_index**](SystemManagementApi.md#set_opensearch_index) | **PUT** /sites/{siteId}/opensearch/index | Set site(s) OpenSearch index settings
[**set_site_group_permissions**](SystemManagementApi.md#set_site_group_permissions) | **PUT** /sites/{siteId}/groups/{groupName}/permissions | Set Site&#39;s Group Permissions
[**update_configuration**](SystemManagementApi.md#update_configuration) | **PATCH** /sites/{siteId}/configuration | Update site configuration
[**update_site**](SystemManagementApi.md#update_site) | **PATCH** /sites/{siteId} | Update Site


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

# **delete_opensearch_index**
> DeleteResponse delete_opensearch_index(site_id)

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
        api_response = api_instance.delete_opensearch_index(site_id)
        print("The response of SystemManagementApi->delete_opensearch_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->delete_opensearch_index: %s\n" % e)
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

# **get_api_keys**
> GetApiKeysResponse get_api_keys(site_id)

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

    try:
        # Get API Keys
        api_response = api_instance.get_api_keys(site_id)
        print("The response of SystemManagementApi->get_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

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

# **get_opensearch_index**
> GetOpenSearchIndexResponse get_opensearch_index(site_id)

Get site(s) OpenSearch index settings

Returns the OpenSearch index settings

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
        api_response = api_instance.get_opensearch_index(site_id)
        print("The response of SystemManagementApi->get_opensearch_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_opensearch_index: %s\n" % e)
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

# **set_opensearch_index**
> SetOpenSearchIndexResponse set_opensearch_index(site_id, set_open_search_index_request)

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
        api_response = api_instance.set_opensearch_index(site_id, set_open_search_index_request)
        print("The response of SystemManagementApi->set_opensearch_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->set_opensearch_index: %s\n" % e)
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

