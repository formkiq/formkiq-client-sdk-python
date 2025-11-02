# openapi_client.AttributesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_attribute**](AttributesApi.md#add_attribute) | **POST** /attributes | Add new attribute
[**delete_attribute**](AttributesApi.md#delete_attribute) | **DELETE** /attributes/{key} | Delete attribute
[**get_attribute**](AttributesApi.md#get_attribute) | **GET** /attributes/{key} | Get Attribute
[**get_attribute_allowed_values**](AttributesApi.md#get_attribute_allowed_values) | **GET** /attributes/{key}/allowedValues | Get Attribute Allowed Values
[**get_attributes**](AttributesApi.md#get_attributes) | **GET** /attributes | Get Attributes listing
[**update_attribute**](AttributesApi.md#update_attribute) | **PATCH** /attributes/{key} | Update existing attribute


# **add_attribute**
> AddResponse add_attribute(add_attribute_request, site_id=site_id)

Add new attribute

Creates a new attribute

### Example


```python
import openapi_client
from openapi_client.models.add_attribute_request import AddAttributeRequest
from openapi_client.models.add_response import AddResponse
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
    api_instance = openapi_client.AttributesApi(api_client)
    add_attribute_request = openapi_client.AddAttributeRequest() # AddAttributeRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add new attribute
        api_response = api_instance.add_attribute(add_attribute_request, site_id=site_id)
        print("The response of AttributesApi->add_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->add_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_attribute_request** | [**AddAttributeRequest**](AddAttributeRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

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

# **delete_attribute**
> DeleteResponse delete_attribute(key, site_id=site_id)

Delete attribute

Delete a attribute

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
    api_instance = openapi_client.AttributesApi(api_client)
    key = 'key_example' # str | Key Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete attribute
        api_response = api_instance.delete_attribute(key, site_id=site_id)
        print("The response of AttributesApi->delete_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->delete_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key Identifier | 
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
**400** | 400 OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute**
> GetAttributeResponse get_attribute(key, site_id=site_id)

Get Attribute

Returns a attribute

### Example


```python
import openapi_client
from openapi_client.models.get_attribute_response import GetAttributeResponse
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
    api_instance = openapi_client.AttributesApi(api_client)
    key = 'key_example' # str | Key Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get Attribute
        api_response = api_instance.get_attribute(key, site_id=site_id)
        print("The response of AttributesApi->get_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->get_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetAttributeResponse**](GetAttributeResponse.md)

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

# **get_attribute_allowed_values**
> GetAttributeAllowedValuesResponse get_attribute_allowed_values(key, site_id=site_id)

Get Attribute Allowed Values

Returns an attribute's allowed values that spans across all classifications and site schema

### Example


```python
import openapi_client
from openapi_client.models.get_attribute_allowed_values_response import GetAttributeAllowedValuesResponse
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
    api_instance = openapi_client.AttributesApi(api_client)
    key = 'key_example' # str | Key Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get Attribute Allowed Values
        api_response = api_instance.get_attribute_allowed_values(key, site_id=site_id)
        print("The response of AttributesApi->get_attribute_allowed_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->get_attribute_allowed_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetAttributeAllowedValuesResponse**](GetAttributeAllowedValuesResponse.md)

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

# **get_attributes**
> GetAttributesResponse get_attributes(site_id=site_id, next=next, limit=limit)

Get Attributes listing

Returns a list of attributes

### Example


```python
import openapi_client
from openapi_client.models.get_attributes_response import GetAttributesResponse
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
    api_instance = openapi_client.AttributesApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get Attributes listing
        api_response = api_instance.get_attributes(site_id=site_id, next=next, limit=limit)
        print("The response of AttributesApi->get_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->get_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetAttributesResponse**](GetAttributesResponse.md)

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

# **update_attribute**
> UpdateResponse update_attribute(key, update_attribute_request, site_id=site_id)

Update existing attribute

Updates existing attribute

### Example


```python
import openapi_client
from openapi_client.models.update_attribute_request import UpdateAttributeRequest
from openapi_client.models.update_response import UpdateResponse
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
    api_instance = openapi_client.AttributesApi(api_client)
    key = 'key_example' # str | Key Identifier
    update_attribute_request = openapi_client.UpdateAttributeRequest() # UpdateAttributeRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Update existing attribute
        api_response = api_instance.update_attribute(key, update_attribute_request, site_id=site_id)
        print("The response of AttributesApi->update_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttributesApi->update_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Key Identifier | 
 **update_attribute_request** | [**UpdateAttributeRequest**](UpdateAttributeRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

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

