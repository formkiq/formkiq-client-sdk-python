# formkiq_client.DocumentAttributesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_attributes**](DocumentAttributesApi.md#add_document_attributes) | **POST** /documents/{documentId}/attributes | Add attribute to document
[**delete_document_attribute**](DocumentAttributesApi.md#delete_document_attribute) | **DELETE** /documents/{documentId}/attributes/{attributeKey} | Delete document attribute
[**delete_document_attribute_and_value**](DocumentAttributesApi.md#delete_document_attribute_and_value) | **DELETE** /documents/{documentId}/attributes/{attributeKey}/{attributeValue} | Delete document&#39;s attribute value
[**get_document_attribute**](DocumentAttributesApi.md#get_document_attribute) | **GET** /documents/{documentId}/attributes/{attributeKey} | Get document attribute by key
[**get_document_attribute_versions**](DocumentAttributesApi.md#get_document_attribute_versions) | **GET** /documents/{documentId}/attributes/{attributeKey}/versions | Get document attribute&#39;s versions
[**get_document_attributes**](DocumentAttributesApi.md#get_document_attributes) | **GET** /documents/{documentId}/attributes | Get document&#39;s attributes
[**set_document_attribute_value**](DocumentAttributesApi.md#set_document_attribute_value) | **PUT** /documents/{documentId}/attributes/{attributeKey} | Set document&#39;s attributes value
[**set_document_attributes**](DocumentAttributesApi.md#set_document_attributes) | **PUT** /documents/{documentId}/attributes | Set document&#39;s attributes


# **add_document_attributes**
> AddResponse add_document_attributes(document_id, add_document_attributes_request, site_id=site_id, ws=ws)

Add attribute to document

Add multiple attributes to a document; this endpoint also accepts a different body parameter for adding a single attribute

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_attributes_request import AddDocumentAttributesRequest
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
    api_instance = formkiq_client.DocumentAttributesApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_document_attributes_request = formkiq_client.AddDocumentAttributesRequest() # AddDocumentAttributesRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    ws = 'ws_example' # str | Whether to enable WebSocket real-time communication with the request (optional)

    try:
        # Add attribute to document
        api_response = api_instance.add_document_attributes(document_id, add_document_attributes_request, site_id=site_id, ws=ws)
        print("The response of DocumentAttributesApi->add_document_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttributesApi->add_document_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_document_attributes_request** | [**AddDocumentAttributesRequest**](AddDocumentAttributesRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **ws** | **str**| Whether to enable WebSocket real-time communication with the request | [optional] 

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
**201** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_attribute**
> DeleteResponse delete_document_attribute(document_id, attribute_key, site_id=site_id)

Delete document attribute

Delete a document attribute by using its key

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
    api_instance = formkiq_client.DocumentAttributesApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    attribute_key = 'attribute_key_example' # str | Attribute Key
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete document attribute
        api_response = api_instance.delete_document_attribute(document_id, attribute_key, site_id=site_id)
        print("The response of DocumentAttributesApi->delete_document_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttributesApi->delete_document_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **attribute_key** | **str**| Attribute Key | 
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

# **delete_document_attribute_and_value**
> DeleteResponse delete_document_attribute_and_value(document_id, attribute_key, attribute_value, site_id=site_id)

Delete document's attribute value

Delete a specific document attribute key/value combination; the request will be ignored if there is no valid key/value combination found

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
    api_instance = formkiq_client.DocumentAttributesApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    attribute_key = 'attribute_key_example' # str | Attribute Key
    attribute_value = 'attribute_value_example' # str | Attribute Value
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete document's attribute value
        api_response = api_instance.delete_document_attribute_and_value(document_id, attribute_key, attribute_value, site_id=site_id)
        print("The response of DocumentAttributesApi->delete_document_attribute_and_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttributesApi->delete_document_attribute_and_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **attribute_key** | **str**| Attribute Key | 
 **attribute_value** | **str**| Attribute Value | 
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

# **get_document_attribute**
> GetDocumentAttributeResponse get_document_attribute(document_id, attribute_key, site_id=site_id)

Get document attribute by key

Get a document attribute by using its key

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_attribute_response import GetDocumentAttributeResponse
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
    api_instance = formkiq_client.DocumentAttributesApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    attribute_key = 'attribute_key_example' # str | Attribute Key
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get document attribute by key
        api_response = api_instance.get_document_attribute(document_id, attribute_key, site_id=site_id)
        print("The response of DocumentAttributesApi->get_document_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttributesApi->get_document_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **attribute_key** | **str**| Attribute Key | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetDocumentAttributeResponse**](GetDocumentAttributeResponse.md)

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

# **get_document_attribute_versions**
> GetDocumentAttributeVersionsResponse get_document_attribute_versions(document_id, attribute_key, site_id=site_id, limit=limit, next=next)

Get document attribute's versions

Get a listing of a document's attribute versions; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_attribute_versions_response import GetDocumentAttributeVersionsResponse
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
    api_instance = formkiq_client.DocumentAttributesApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    attribute_key = 'attribute_key_example' # str | Attribute Key
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document attribute's versions
        api_response = api_instance.get_document_attribute_versions(document_id, attribute_key, site_id=site_id, limit=limit, next=next)
        print("The response of DocumentAttributesApi->get_document_attribute_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttributesApi->get_document_attribute_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **attribute_key** | **str**| Attribute Key | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetDocumentAttributeVersionsResponse**](GetDocumentAttributeVersionsResponse.md)

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

# **get_document_attributes**
> GetDocumentAttributesResponse get_document_attributes(document_id, site_id=site_id, limit=limit, next=next)

Get document's attributes

Get a listing of a document's attributes

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_attributes_response import GetDocumentAttributesResponse
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
    api_instance = formkiq_client.DocumentAttributesApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document's attributes
        api_response = api_instance.get_document_attributes(document_id, site_id=site_id, limit=limit, next=next)
        print("The response of DocumentAttributesApi->get_document_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttributesApi->get_document_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetDocumentAttributesResponse**](GetDocumentAttributesResponse.md)

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

# **set_document_attribute_value**
> SetResponse set_document_attribute_value(document_id, attribute_key, set_document_attribute_request, site_id=site_id)

Set document's attributes value

Set attributes value to a document

### Example


```python
import formkiq_client
from formkiq_client.models.set_document_attribute_request import SetDocumentAttributeRequest
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
    api_instance = formkiq_client.DocumentAttributesApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    attribute_key = 'attribute_key_example' # str | Attribute Key
    set_document_attribute_request = formkiq_client.SetDocumentAttributeRequest() # SetDocumentAttributeRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Set document's attributes value
        api_response = api_instance.set_document_attribute_value(document_id, attribute_key, set_document_attribute_request, site_id=site_id)
        print("The response of DocumentAttributesApi->set_document_attribute_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttributesApi->set_document_attribute_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **attribute_key** | **str**| Attribute Key | 
 **set_document_attribute_request** | [**SetDocumentAttributeRequest**](SetDocumentAttributeRequest.md)|  | 
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
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_document_attributes**
> SetResponse set_document_attributes(document_id, set_document_attributes_request, site_id=site_id)

Set document's attributes

Set multiple attributes to a document; this endpoint also accepts a different body parameter for setting a single attribute

Note:
- attributes in the request will overwrite existing attributes.

### Example


```python
import formkiq_client
from formkiq_client.models.set_document_attributes_request import SetDocumentAttributesRequest
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
    api_instance = formkiq_client.DocumentAttributesApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    set_document_attributes_request = formkiq_client.SetDocumentAttributesRequest() # SetDocumentAttributesRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Set document's attributes
        api_response = api_instance.set_document_attributes(document_id, set_document_attributes_request, site_id=site_id)
        print("The response of DocumentAttributesApi->set_document_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentAttributesApi->set_document_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **set_document_attributes_request** | [**SetDocumentAttributesRequest**](SetDocumentAttributesRequest.md)|  | 
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
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

