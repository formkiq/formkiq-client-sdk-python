# formkiq_client.PublicApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_add_document**](PublicApi.md#public_add_document) | **POST** /public/documents | Public add document
[**public_add_webhook**](PublicApi.md#public_add_webhook) | **POST** /public/webhooks/{webhooks+} | Public add webhook


# **public_add_document**
> AddDocumentResponse public_add_document(add_document_request, site_id=site_id)

Public add document

Allow unauthenticated creation of new documents; must be enabled during installation (disabled by default)  See POST /documents/{documentId}/tags for adding tags to document schema  See POST /documents/{documentId}/actions for adding actions to document schema

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_request import AddDocumentRequest
from formkiq_client.models.add_document_response import AddDocumentResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.PublicApi(api_client)
    add_document_request = formkiq_client.AddDocumentRequest() # AddDocumentRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Public add document
        api_response = api_instance.public_add_document(add_document_request, site_id=site_id)
        print("The response of PublicApi->public_add_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_add_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_document_request** | [**AddDocumentRequest**](AddDocumentRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddDocumentResponse**](AddDocumentResponse.md)

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

# **public_add_webhook**
> DocumentId public_add_webhook(webhooks, body, site_id=site_id)

Public add webhook

Receive an incoming public post to a specified webhook and creates a document based on the data sent; must be enabled during installation (disabled by default)

### Example


```python
import formkiq_client
from formkiq_client.models.document_id import DocumentId
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.PublicApi(api_client)
    webhooks = 'webhooks_example' # str | Web Hook Param
    body = None # object | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Public add webhook
        api_response = api_instance.public_add_webhook(webhooks, body, site_id=site_id)
        print("The response of PublicApi->public_add_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->public_add_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhooks** | **str**| Web Hook Param | 
 **body** | **object**|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DocumentId**](DocumentId.md)

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

