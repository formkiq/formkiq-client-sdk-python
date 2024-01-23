# formkiq_client.DocumentVersionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document_version**](DocumentVersionsApi.md#delete_document_version) | **DELETE** /documents/{documentId}/versions/{versionKey} | Delete document version
[**get_document_versions**](DocumentVersionsApi.md#get_document_versions) | **GET** /documents/{documentId}/versions | Get document&#39;s versions
[**set_document_version**](DocumentVersionsApi.md#set_document_version) | **PUT** /documents/{documentId}/versions | Set version of document


# **delete_document_version**
> delete_document_version(document_id, version_key, site_id=site_id, share_key=share_key)

Delete document version

Delete a specific previous document version; ONLY available with FormKiQ Pro and Enterprise

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
    api_instance = formkiq_client.DocumentVersionsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    version_key = 'version_key_example' # str | Version Key
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Delete document version
        api_instance.delete_document_version(document_id, version_key, site_id=site_id, share_key=share_key)
    except Exception as e:
        print("Exception when calling DocumentVersionsApi->delete_document_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **version_key** | **str**| Version Key | 
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

# **get_document_versions**
> GetDocumentVersionsResponse get_document_versions(document_id, site_id=site_id, share_key=share_key, next=next)

Get document's versions

Get a listing of document content and metadata versions; ONLY available with FormKiQ Pro and Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.get_document_versions_response import GetDocumentVersionsResponse
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
    api_instance = formkiq_client.DocumentVersionsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document's versions
        api_response = api_instance.get_document_versions(document_id, site_id=site_id, share_key=share_key, next=next)
        print("The response of DocumentVersionsApi->get_document_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentVersionsApi->get_document_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetDocumentVersionsResponse**](GetDocumentVersionsResponse.md)

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

# **set_document_version**
> SetDocumentVersionResponse set_document_version(document_id, set_document_version_request, site_id=site_id)

Set version of document

Set document to a previous document version; ONLY available with FormKiQ Pro and Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.set_document_version_request import SetDocumentVersionRequest
from formkiq_client.models.set_document_version_response import SetDocumentVersionResponse
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
    api_instance = formkiq_client.DocumentVersionsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    set_document_version_request = formkiq_client.SetDocumentVersionRequest() # SetDocumentVersionRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Set version of document
        api_response = api_instance.set_document_version(document_id, set_document_version_request, site_id=site_id)
        print("The response of DocumentVersionsApi->set_document_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentVersionsApi->set_document_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **set_document_version_request** | [**SetDocumentVersionRequest**](SetDocumentVersionRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**SetDocumentVersionResponse**](SetDocumentVersionResponse.md)

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

