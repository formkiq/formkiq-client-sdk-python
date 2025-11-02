# openapi_client.MappingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_mapping**](MappingsApi.md#add_mapping) | **POST** /mappings | Add New Mapping
[**delete_mapping**](MappingsApi.md#delete_mapping) | **DELETE** /mappings/{mappingId} | Delete Mapping
[**get_mapping**](MappingsApi.md#get_mapping) | **GET** /mappings/{mappingId} | Get Mapping
[**get_mappings**](MappingsApi.md#get_mappings) | **GET** /mappings | Get Mappings
[**set_mapping**](MappingsApi.md#set_mapping) | **PUT** /mappings/{mappingId} | Set Mapping


# **add_mapping**
> AddMappingResponse add_mapping(add_mapping_request, site_id=site_id)

Add New Mapping

Creates a new mapping; available as an Add-On Module

### Example


```python
import openapi_client
from openapi_client.models.add_mapping_request import AddMappingRequest
from openapi_client.models.add_mapping_response import AddMappingResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MappingsApi(api_client)
    add_mapping_request = openapi_client.AddMappingRequest() # AddMappingRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add New Mapping
        api_response = api_instance.add_mapping(add_mapping_request, site_id=site_id)
        print("The response of MappingsApi->add_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingsApi->add_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_mapping_request** | [**AddMappingRequest**](AddMappingRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddMappingResponse**](AddMappingResponse.md)

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

# **delete_mapping**
> DeleteResponse delete_mapping(mapping_id, site_id=site_id)

Delete Mapping

Delete Mapping; available as an Add-On Module

### Example


```python
import openapi_client
from openapi_client.models.delete_response import DeleteResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MappingsApi(api_client)
    mapping_id = 'mapping_id_example' # str | Mapping Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete Mapping
        api_response = api_instance.delete_mapping(mapping_id, site_id=site_id)
        print("The response of MappingsApi->delete_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingsApi->delete_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **str**| Mapping Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

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

# **get_mapping**
> GetMappingResponse get_mapping(mapping_id, site_id=site_id)

Get Mapping

Get a mapping; available as an Add-On Module

### Example


```python
import openapi_client
from openapi_client.models.get_mapping_response import GetMappingResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MappingsApi(api_client)
    mapping_id = 'mapping_id_example' # str | Mapping Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get Mapping
        api_response = api_instance.get_mapping(mapping_id, site_id=site_id)
        print("The response of MappingsApi->get_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingsApi->get_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **str**| Mapping Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetMappingResponse**](GetMappingResponse.md)

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

# **get_mappings**
> GetMappingsResponse get_mappings(site_id=site_id, limit=limit, next=next)

Get Mappings

Returns a list of mappings; available as an Add-On Module

### Example


```python
import openapi_client
from openapi_client.models.get_mappings_response import GetMappingsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MappingsApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get Mappings
        api_response = api_instance.get_mappings(site_id=site_id, limit=limit, next=next)
        print("The response of MappingsApi->get_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingsApi->get_mappings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetMappingsResponse**](GetMappingsResponse.md)

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

# **set_mapping**
> SetResponse set_mapping(mapping_id, set_mapping_request, site_id=site_id)

Set Mapping

Sets an mapping; available as an Add-On Module

### Example


```python
import openapi_client
from openapi_client.models.set_mapping_request import SetMappingRequest
from openapi_client.models.set_response import SetResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.MappingsApi(api_client)
    mapping_id = 'mapping_id_example' # str | Mapping Identifier
    set_mapping_request = openapi_client.SetMappingRequest() # SetMappingRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Set Mapping
        api_response = api_instance.set_mapping(mapping_id, set_mapping_request, site_id=site_id)
        print("The response of MappingsApi->set_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MappingsApi->set_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **str**| Mapping Identifier | 
 **set_mapping_request** | [**SetMappingRequest**](SetMappingRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

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
**200** | 200 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

