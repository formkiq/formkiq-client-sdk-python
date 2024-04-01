# formkiq_client.AccessControlApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_access_attributes**](AccessControlApi.md#add_document_access_attributes) | **POST** /documents/{documentId}/accessAttributes | Add document access attributes
[**delete_document_access_attributes**](AccessControlApi.md#delete_document_access_attributes) | **DELETE** /documents/{documentId}/accessAttributes | Delete document&#39;s access attributes
[**delete_opa_configuration**](AccessControlApi.md#delete_opa_configuration) | **DELETE** /sites/{siteId}/opa/accessPolicy | Delete OPA Configuration
[**get_document_access_attributes**](AccessControlApi.md#get_document_access_attributes) | **GET** /documents/{documentId}/accessAttributes | Get document access attributes
[**get_opa_configuration**](AccessControlApi.md#get_opa_configuration) | **GET** /sites/{siteId}/opa/accessPolicy | Get OPA Configuration
[**get_opa_configurations**](AccessControlApi.md#get_opa_configurations) | **GET** /sites/opa/accessPolicies | Get OPAs Configuration
[**set_document_access_attributes**](AccessControlApi.md#set_document_access_attributes) | **PUT** /documents/{documentId}/accessAttributes | Set document access attributes
[**set_opa_configuration**](AccessControlApi.md#set_opa_configuration) | **PUT** /sites/opa/accessPolicies | Set OPA Configuration


# **add_document_access_attributes**
> AddDocumentAccessAttributesResponse add_document_access_attributes(document_id, add_document_access_attributes_request, site_id=site_id)

Add document access attributes

Add a document's access attributes (only \"admin\" role can call API)

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_access_attributes_request import AddDocumentAccessAttributesRequest
from formkiq_client.models.add_document_access_attributes_response import AddDocumentAccessAttributesResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_document_access_attributes_request = formkiq_client.AddDocumentAccessAttributesRequest() # AddDocumentAccessAttributesRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add document access attributes
        api_response = api_instance.add_document_access_attributes(document_id, add_document_access_attributes_request, site_id=site_id)
        print("The response of AccessControlApi->add_document_access_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->add_document_access_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_document_access_attributes_request** | [**AddDocumentAccessAttributesRequest**](AddDocumentAccessAttributesRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddDocumentAccessAttributesResponse**](AddDocumentAccessAttributesResponse.md)

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

# **delete_document_access_attributes**
> DeleteDocumentAccessAttributesResponse delete_document_access_attributes(document_id, site_id=site_id)

Delete document's access attributes

Delete a document's access attributes

### Example


```python
import formkiq_client
from formkiq_client.models.delete_document_access_attributes_response import DeleteDocumentAccessAttributesResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete document's access attributes
        api_response = api_instance.delete_document_access_attributes(document_id, site_id=site_id)
        print("The response of AccessControlApi->delete_document_access_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->delete_document_access_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteDocumentAccessAttributesResponse**](DeleteDocumentAccessAttributesResponse.md)

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

# **delete_opa_configuration**
> DeleteOpaConfigurationResponse delete_opa_configuration(site_id)

Delete OPA Configuration

Delete OPA Configuration

### Example


```python
import formkiq_client
from formkiq_client.models.delete_opa_configuration_response import DeleteOpaConfigurationResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Delete OPA Configuration
        api_response = api_instance.delete_opa_configuration(site_id)
        print("The response of AccessControlApi->delete_opa_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->delete_opa_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**DeleteOpaConfigurationResponse**](DeleteOpaConfigurationResponse.md)

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

# **get_document_access_attributes**
> GetDocumentAccessAttributesResponse get_document_access_attributes(document_id, site_id=site_id)

Get document access attributes

Retrieves a document's access attributes (only \"admin\" role can call API)

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_access_attributes_response import GetDocumentAccessAttributesResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get document access attributes
        api_response = api_instance.get_document_access_attributes(document_id, site_id=site_id)
        print("The response of AccessControlApi->get_document_access_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_document_access_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetDocumentAccessAttributesResponse**](GetDocumentAccessAttributesResponse.md)

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

# **get_opa_configuration**
> GetOpaConfigurationResponse get_opa_configuration(site_id)

Get OPA Configuration

Returns OPA Configuration, can only be requested with ADMIN privileges

### Example


```python
import formkiq_client
from formkiq_client.models.get_opa_configuration_response import GetOpaConfigurationResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Get OPA Configuration
        api_response = api_instance.get_opa_configuration(site_id)
        print("The response of AccessControlApi->get_opa_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_opa_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**GetOpaConfigurationResponse**](GetOpaConfigurationResponse.md)

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

# **get_opa_configurations**
> GetOpaConfigurationsResponse get_opa_configurations()

Get OPAs Configuration

Returns a list of OPA Configuration, can only be requested with ADMIN privileges

### Example


```python
import formkiq_client
from formkiq_client.models.get_opa_configurations_response import GetOpaConfigurationsResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)

    try:
        # Get OPAs Configuration
        api_response = api_instance.get_opa_configurations()
        print("The response of AccessControlApi->get_opa_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_opa_configurations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOpaConfigurationsResponse**](GetOpaConfigurationsResponse.md)

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

# **set_document_access_attributes**
> SetDocumentAccessAttributesResponse set_document_access_attributes(document_id, set_document_access_attributes_request, site_id=site_id)

Set document access attributes

Set a document's access attributes (only \"admin\" role can call API)

### Example


```python
import formkiq_client
from formkiq_client.models.set_document_access_attributes_request import SetDocumentAccessAttributesRequest
from formkiq_client.models.set_document_access_attributes_response import SetDocumentAccessAttributesResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    set_document_access_attributes_request = formkiq_client.SetDocumentAccessAttributesRequest() # SetDocumentAccessAttributesRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Set document access attributes
        api_response = api_instance.set_document_access_attributes(document_id, set_document_access_attributes_request, site_id=site_id)
        print("The response of AccessControlApi->set_document_access_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->set_document_access_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **set_document_access_attributes_request** | [**SetDocumentAccessAttributesRequest**](SetDocumentAccessAttributesRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**SetDocumentAccessAttributesResponse**](SetDocumentAccessAttributesResponse.md)

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

# **set_opa_configuration**
> SetOpaConfigurationResponse set_opa_configuration(set_opa_configuration_request)

Set OPA Configuration

Set OPA Configuration, can only be requested with ADMIN privileges

### Example


```python
import formkiq_client
from formkiq_client.models.set_opa_configuration_request import SetOpaConfigurationRequest
from formkiq_client.models.set_opa_configuration_response import SetOpaConfigurationResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)
    set_opa_configuration_request = formkiq_client.SetOpaConfigurationRequest() # SetOpaConfigurationRequest | 

    try:
        # Set OPA Configuration
        api_response = api_instance.set_opa_configuration(set_opa_configuration_request)
        print("The response of AccessControlApi->set_opa_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->set_opa_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_opa_configuration_request** | [**SetOpaConfigurationRequest**](SetOpaConfigurationRequest.md)|  | 

### Return type

[**SetOpaConfigurationResponse**](SetOpaConfigurationResponse.md)

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

