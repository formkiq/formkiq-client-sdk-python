# formkiq_client.SystemManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_api_key**](SystemManagementApi.md#add_api_key) | **POST** /configuration/apiKeys | Add API Key
[**delete_api_key**](SystemManagementApi.md#delete_api_key) | **DELETE** /configuration/apiKeys/{apiKey} | Delete API Key
[**get_api_keys**](SystemManagementApi.md#get_api_keys) | **GET** /configuration/apiKeys | Get API Keys
[**get_configuration**](SystemManagementApi.md#get_configuration) | **GET** /configuration | Get site configuration
[**get_sites**](SystemManagementApi.md#get_sites) | **GET** /sites | Get site(s) access
[**get_version**](SystemManagementApi.md#get_version) | **GET** /version | Get FormKiQ version
[**update_configuration**](SystemManagementApi.md#update_configuration) | **PATCH** /configuration | Update site configuration


# **add_api_key**
> AddApiKeyResponse add_api_key(add_api_key_request, site_id=site_id)

Add API Key

Adds a new API Key

### Example


```python
import time
import os
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
    add_api_key_request = {"name":"My API Key"} # AddApiKeyRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add API Key
        api_response = api_instance.add_api_key(add_api_key_request, site_id=site_id)
        print("The response of SystemManagementApi->add_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->add_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_api_key_request** | [**AddApiKeyRequest**](AddApiKeyRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

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

# **delete_api_key**
> DeleteApiKeyResponse delete_api_key(api_key, site_id=site_id)

Delete API Key

Adds a new API Key

### Example


```python
import time
import os
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
    api_key = 'api_key_example' # str | API Key
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete API Key
        api_response = api_instance.delete_api_key(api_key, site_id=site_id)
        print("The response of SystemManagementApi->delete_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| API Key | 
 **site_id** | **str**| Site Identifier | [optional] 

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

# **get_api_keys**
> GetApiKeysResponse get_api_keys(site_id=site_id)

Get API Keys

Returns the list of ApiKeys

### Example


```python
import time
import os
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
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get API Keys
        api_response = api_instance.get_api_keys(site_id=site_id)
        print("The response of SystemManagementApi->get_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_api_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 

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
> GetConfigurationResponse get_configuration(site_id=site_id)

Get site configuration

Returns the list of sites that the user has access to

### Example


```python
import time
import os
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
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get site configuration
        api_response = api_instance.get_configuration(site_id=site_id)
        print("The response of SystemManagementApi->get_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 

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

# **get_sites**
> GetSitesResponse get_sites()

Get site(s) access

Returns the list of sites that the user has access to

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.get_sites_response import GetSitesResponse
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
        # Get site(s) access
        api_response = api_instance.get_sites()
        print("The response of SystemManagementApi->get_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->get_sites: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
import time
import os
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

# **update_configuration**
> UpdateConfigurationResponse update_configuration(update_configuration_request, site_id=site_id)

Update site configuration

Update the System Management configuration

### Example


```python
import time
import os
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
    update_configuration_request = {"chatGptApiKey":"ABC","maxContentLengthBytes":"1000000","maxDocuments":"1000","maxWebhooks":"10","notificationEmail":"<email>"} # UpdateConfigurationRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Update site configuration
        api_response = api_instance.update_configuration(update_configuration_request, site_id=site_id)
        print("The response of SystemManagementApi->update_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemManagementApi->update_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_configuration_request** | [**UpdateConfigurationRequest**](UpdateConfigurationRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

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

