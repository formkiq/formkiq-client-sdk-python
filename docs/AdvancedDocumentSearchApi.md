# formkiq_client.AdvancedDocumentSearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document_fulltext**](AdvancedDocumentSearchApi.md#delete_document_fulltext) | **DELETE** /documents/{documentId}/fulltext | Delete document full-text
[**delete_document_fulltext_tag**](AdvancedDocumentSearchApi.md#delete_document_fulltext_tag) | **DELETE** /documents/{documentId}/fulltext/tags/{tagKey} | Delete document full-text tag
[**delete_document_fulltext_tag_and_value**](AdvancedDocumentSearchApi.md#delete_document_fulltext_tag_and_value) | **DELETE** /documents/{documentId}/fulltext/tags/{tagKey}/{tagValue} | Delete document full-text tag/value
[**document_fulltext**](AdvancedDocumentSearchApi.md#document_fulltext) | **POST** /searchFulltext | Document full-text search
[**get_document_fulltext**](AdvancedDocumentSearchApi.md#get_document_fulltext) | **GET** /documents/{documentId}/fulltext | Get document&#39;s full-text
[**query_fulltext**](AdvancedDocumentSearchApi.md#query_fulltext) | **POST** /queryFulltext | Direct opensearch search API
[**set_document_fulltext**](AdvancedDocumentSearchApi.md#set_document_fulltext) | **PUT** /documents/{documentId}/fulltext | Set document&#39;s full-text
[**update_document_fulltext**](AdvancedDocumentSearchApi.md#update_document_fulltext) | **PATCH** /documents/{documentId}/fulltext | Update document&#39;s full-text


# **delete_document_fulltext**
> DeleteFulltextResponse delete_document_fulltext(document_id, site_id=site_id)

Delete document full-text

Remove full text search for a document from OpenSearch; ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.delete_fulltext_response import DeleteFulltextResponse
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
    api_instance = formkiq_client.AdvancedDocumentSearchApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete document full-text
        api_response = api_instance.delete_document_fulltext(document_id, site_id=site_id)
        print("The response of AdvancedDocumentSearchApi->delete_document_fulltext:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvancedDocumentSearchApi->delete_document_fulltext: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteFulltextResponse**](DeleteFulltextResponse.md)

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

# **delete_document_fulltext_tag**
> delete_document_fulltext_tag(document_id, tag_key, site_id=site_id, share_key=share_key)

Delete document full-text tag

Remove document tags from OpenSearch; ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
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
    api_instance = formkiq_client.AdvancedDocumentSearchApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    tag_key = 'tag_key_example' # str | Tag Key
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Delete document full-text tag
        api_instance.delete_document_fulltext_tag(document_id, tag_key, site_id=site_id, share_key=share_key)
    except Exception as e:
        print("Exception when calling AdvancedDocumentSearchApi->delete_document_fulltext_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **tag_key** | **str**| Tag Key | 
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

# **delete_document_fulltext_tag_and_value**
> delete_document_fulltext_tag_and_value(document_id, tag_key, tag_value, site_id=site_id, share_key=share_key)

Delete document full-text tag/value

Remove document tag/value from OpenSearch; ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
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
    api_instance = formkiq_client.AdvancedDocumentSearchApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    tag_key = 'tag_key_example' # str | Tag Key
    tag_value = 'tag_value_example' # str | Tag Key Value
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Delete document full-text tag/value
        api_instance.delete_document_fulltext_tag_and_value(document_id, tag_key, tag_value, site_id=site_id, share_key=share_key)
    except Exception as e:
        print("Exception when calling AdvancedDocumentSearchApi->delete_document_fulltext_tag_and_value: %s\n" % e)
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

# **document_fulltext**
> DocumentFulltextResponse document_fulltext(document_fulltext_request, site_id=site_id, limit=limit)

Document full-text search

Document full-text search (and more robust multi-tag search queries, powered by OpenSearch); ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.document_fulltext_request import DocumentFulltextRequest
from formkiq_client.models.document_fulltext_response import DocumentFulltextResponse
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
    api_instance = formkiq_client.AdvancedDocumentSearchApi(api_client)
    document_fulltext_request = formkiq_client.DocumentFulltextRequest() # DocumentFulltextRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Document full-text search
        api_response = api_instance.document_fulltext(document_fulltext_request, site_id=site_id, limit=limit)
        print("The response of AdvancedDocumentSearchApi->document_fulltext:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvancedDocumentSearchApi->document_fulltext: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_fulltext_request** | [**DocumentFulltextRequest**](DocumentFulltextRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**DocumentFulltextResponse**](DocumentFulltextResponse.md)

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

# **get_document_fulltext**
> GetDocumentFulltextResponse get_document_fulltext(document_id, site_id=site_id, share_key=share_key)

Get document's full-text

Retrieve an OpenSearch document's details, i.e., metadata

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.get_document_fulltext_response import GetDocumentFulltextResponse
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
    api_instance = formkiq_client.AdvancedDocumentSearchApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Get document's full-text
        api_response = api_instance.get_document_fulltext(document_id, site_id=site_id, share_key=share_key)
        print("The response of AdvancedDocumentSearchApi->get_document_fulltext:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvancedDocumentSearchApi->get_document_fulltext: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**GetDocumentFulltextResponse**](GetDocumentFulltextResponse.md)

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

# **query_fulltext**
> QueryFulltextResponse query_fulltext(body, site_id=site_id)

Direct opensearch search API

Endpoint for allowing custom, complex queries using the OpenSearch search API (https://opensearch.org/docs/latest/opensearch/rest-api/search/); ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.query_fulltext_response import QueryFulltextResponse
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
    api_instance = formkiq_client.AdvancedDocumentSearchApi(api_client)
    body = None # object | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Direct opensearch search API
        api_response = api_instance.query_fulltext(body, site_id=site_id)
        print("The response of AdvancedDocumentSearchApi->query_fulltext:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvancedDocumentSearchApi->query_fulltext: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**QueryFulltextResponse**](QueryFulltextResponse.md)

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

# **set_document_fulltext**
> SetDocumentFulltextResponse set_document_fulltext(document_id, site_id=site_id, set_document_fulltext_request=set_document_fulltext_request)

Set document's full-text

Set all text/tags found within a document to OpenSearch; ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.set_document_fulltext_request import SetDocumentFulltextRequest
from formkiq_client.models.set_document_fulltext_response import SetDocumentFulltextResponse
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
    api_instance = formkiq_client.AdvancedDocumentSearchApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    set_document_fulltext_request = formkiq_client.SetDocumentFulltextRequest() # SetDocumentFulltextRequest |  (optional)

    try:
        # Set document's full-text
        api_response = api_instance.set_document_fulltext(document_id, site_id=site_id, set_document_fulltext_request=set_document_fulltext_request)
        print("The response of AdvancedDocumentSearchApi->set_document_fulltext:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvancedDocumentSearchApi->set_document_fulltext: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **set_document_fulltext_request** | [**SetDocumentFulltextRequest**](SetDocumentFulltextRequest.md)|  | [optional] 

### Return type

[**SetDocumentFulltextResponse**](SetDocumentFulltextResponse.md)

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

# **update_document_fulltext**
> SetDocumentFulltextResponse update_document_fulltext(document_id, site_id=site_id, update_document_fulltext_request=update_document_fulltext_request)

Update document's full-text

Update a document in OpenSearch; ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.set_document_fulltext_response import SetDocumentFulltextResponse
from formkiq_client.models.update_document_fulltext_request import UpdateDocumentFulltextRequest
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
    api_instance = formkiq_client.AdvancedDocumentSearchApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    update_document_fulltext_request = formkiq_client.UpdateDocumentFulltextRequest() # UpdateDocumentFulltextRequest |  (optional)

    try:
        # Update document's full-text
        api_response = api_instance.update_document_fulltext(document_id, site_id=site_id, update_document_fulltext_request=update_document_fulltext_request)
        print("The response of AdvancedDocumentSearchApi->update_document_fulltext:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvancedDocumentSearchApi->update_document_fulltext: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **update_document_fulltext_request** | [**UpdateDocumentFulltextRequest**](UpdateDocumentFulltextRequest.md)|  | [optional] 

### Return type

[**SetDocumentFulltextResponse**](SetDocumentFulltextResponse.md)

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

