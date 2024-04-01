# formkiq_client.DocumentTagsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_tags**](DocumentTagsApi.md#add_document_tags) | **POST** /documents/{documentId}/tags | Add tag to document
[**delete_document_tag**](DocumentTagsApi.md#delete_document_tag) | **DELETE** /documents/{documentId}/tags/{tagKey} | Delete document tag
[**delete_document_tag_and_value**](DocumentTagsApi.md#delete_document_tag_and_value) | **DELETE** /documents/{documentId}/tags/{tagKey}/{tagValue} | Delete document&#39;s tag value
[**get_document_tag**](DocumentTagsApi.md#get_document_tag) | **GET** /documents/{documentId}/tags/{tagKey} | Get document tag by key
[**get_document_tags**](DocumentTagsApi.md#get_document_tags) | **GET** /documents/{documentId}/tags | Get document&#39;s tags
[**set_document_tag**](DocumentTagsApi.md#set_document_tag) | **PUT** /documents/{documentId}/tags/{tagKey} | Update document tag value(s)
[**set_document_tags**](DocumentTagsApi.md#set_document_tags) | **PUT** /documents/{documentId}/tags | Set document&#39;s tags
[**update_document_tags**](DocumentTagsApi.md#update_document_tags) | **PATCH** /documents/{documentId}/tags | Update document tags
[**update_matching_document_tags**](DocumentTagsApi.md#update_matching_document_tags) | **PATCH** /documents/tags | Mass Update document tag(s)


# **add_document_tags**
> add_document_tags(document_id, add_document_tags_request, site_id=site_id, ws=ws)

Add tag to document

Add multiple tags to a document; this endpoint also accepts a different body parameter for adding a single tag

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_tags_request import AddDocumentTagsRequest
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
    api_instance = formkiq_client.DocumentTagsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_document_tags_request = {"key":"category"} # AddDocumentTagsRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    ws = 'ws_example' # str | Whether to enable WebSocket real-time communication with the request (optional)

    try:
        # Add tag to document
        api_instance.add_document_tags(document_id, add_document_tags_request, site_id=site_id, ws=ws)
    except Exception as e:
        print("Exception when calling DocumentTagsApi->add_document_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_document_tags_request** | [**AddDocumentTagsRequest**](AddDocumentTagsRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **ws** | **str**| Whether to enable WebSocket real-time communication with the request | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_tag**
> delete_document_tag(document_id, tag_key, site_id=site_id)

Delete document tag

Delete a document tag by using its key

### Example


```python
import formkiq_client
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
    api_instance = formkiq_client.DocumentTagsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    tag_key = 'tag_key_example' # str | Tag Key
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete document tag
        api_instance.delete_document_tag(document_id, tag_key, site_id=site_id)
    except Exception as e:
        print("Exception when calling DocumentTagsApi->delete_document_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **tag_key** | **str**| Tag Key | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_tag_and_value**
> delete_document_tag_and_value(document_id, tag_key, tag_value, site_id=site_id, share_key=share_key)

Delete document's tag value

Delete a specific document tag's key/value combination; the request will be ignored if there is no valid key/value combination found

### Example


```python
import formkiq_client
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
    api_instance = formkiq_client.DocumentTagsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    tag_key = 'tag_key_example' # str | Tag Key
    tag_value = 'tag_value_example' # str | Tag Key Value
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Delete document's tag value
        api_instance.delete_document_tag_and_value(document_id, tag_key, tag_value, site_id=site_id, share_key=share_key)
    except Exception as e:
        print("Exception when calling DocumentTagsApi->delete_document_tag_and_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **tag_key** | **str**| Tag Key | 
 **tag_value** | **str**| Tag Key Value | 
 **site_id** | **str**| Site Identifier | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_tag**
> GetDocumentTagResponse get_document_tag(document_id, tag_key, site_id=site_id, share_key=share_key)

Get document tag by key

Get a document tag by using its key

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_tag_response import GetDocumentTagResponse
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
    api_instance = formkiq_client.DocumentTagsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    tag_key = 'tag_key_example' # str | Tag Key
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Get document tag by key
        api_response = api_instance.get_document_tag(document_id, tag_key, site_id=site_id, share_key=share_key)
        print("The response of DocumentTagsApi->get_document_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentTagsApi->get_document_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **tag_key** | **str**| Tag Key | 
 **site_id** | **str**| Site Identifier | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**GetDocumentTagResponse**](GetDocumentTagResponse.md)

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

# **get_document_tags**
> GetDocumentTagsResponse get_document_tags(document_id, site_id=site_id, limit=limit, share_key=share_key, next=next, previous=previous)

Get document's tags

Get a listing of a document's tags

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_tags_response import GetDocumentTagsResponse
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
    api_instance = formkiq_client.DocumentTagsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    share_key = 'share_key_example' # str | Share Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    previous = 'previous_example' # str | Previous page of results token (optional)

    try:
        # Get document's tags
        api_response = api_instance.get_document_tags(document_id, site_id=site_id, limit=limit, share_key=share_key, next=next, previous=previous)
        print("The response of DocumentTagsApi->get_document_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentTagsApi->get_document_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **share_key** | **str**| Share Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **previous** | **str**| Previous page of results token | [optional] 

### Return type

[**GetDocumentTagsResponse**](GetDocumentTagsResponse.md)

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

# **set_document_tag**
> set_document_tag(document_id, tag_key, set_document_tag_key_request, site_id=site_id)

Update document tag value(s)

Update any and all values of a document tag, by using its key; you can supply one tag value or a list of tag values in the request body

### Example


```python
import formkiq_client
from formkiq_client.models.set_document_tag_key_request import SetDocumentTagKeyRequest
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
    api_instance = formkiq_client.DocumentTagsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    tag_key = 'tag_key_example' # str | Tag Key
    set_document_tag_key_request = formkiq_client.SetDocumentTagKeyRequest() # SetDocumentTagKeyRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Update document tag value(s)
        api_instance.set_document_tag(document_id, tag_key, set_document_tag_key_request, site_id=site_id)
    except Exception as e:
        print("Exception when calling DocumentTagsApi->set_document_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **tag_key** | **str**| Tag Key | 
 **set_document_tag_key_request** | [**SetDocumentTagKeyRequest**](SetDocumentTagKeyRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_document_tags**
> set_document_tags(document_id, add_document_tags_request, site_id=site_id)

Set document's tags

Set multiple tags to a document; this endpoint also accepts a different body parameter for setting a single tag

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_tags_request import AddDocumentTagsRequest
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
    api_instance = formkiq_client.DocumentTagsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_document_tags_request = {"tags":[{"key":"category"}]} # AddDocumentTagsRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Set document's tags
        api_instance.set_document_tags(document_id, add_document_tags_request, site_id=site_id)
    except Exception as e:
        print("Exception when calling DocumentTagsApi->set_document_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_document_tags_request** | [**AddDocumentTagsRequest**](AddDocumentTagsRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document_tags**
> update_document_tags(document_id, add_document_tags_request, site_id=site_id)

Update document tags

Updates multiple tags to a document; this endpoint also accepts a different body parameter for updating a single tag

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_tags_request import AddDocumentTagsRequest
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
    api_instance = formkiq_client.DocumentTagsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_document_tags_request = {"tags":[{"key":"category"}]} # AddDocumentTagsRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Update document tags
        api_instance.update_document_tags(document_id, add_document_tags_request, site_id=site_id)
    except Exception as e:
        print("Exception when calling DocumentTagsApi->update_document_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_document_tags_request** | [**AddDocumentTagsRequest**](AddDocumentTagsRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_matching_document_tags**
> UpdateMatchingDocumentTagsResponse update_matching_document_tags(update_matching_document_tags_request, site_id=site_id)

Mass Update document tag(s)

This API request allows the adding/updating of multiple document tag(s) based on document(s) that have the matching tag.

### Example


```python
import formkiq_client
from formkiq_client.models.update_matching_document_tags_request import UpdateMatchingDocumentTagsRequest
from formkiq_client.models.update_matching_document_tags_response import UpdateMatchingDocumentTagsResponse
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
    api_instance = formkiq_client.DocumentTagsApi(api_client)
    update_matching_document_tags_request = formkiq_client.UpdateMatchingDocumentTagsRequest() # UpdateMatchingDocumentTagsRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Mass Update document tag(s)
        api_response = api_instance.update_matching_document_tags(update_matching_document_tags_request, site_id=site_id)
        print("The response of DocumentTagsApi->update_matching_document_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentTagsApi->update_matching_document_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_matching_document_tags_request** | [**UpdateMatchingDocumentTagsRequest**](UpdateMatchingDocumentTagsRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**UpdateMatchingDocumentTagsResponse**](UpdateMatchingDocumentTagsResponse.md)

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

