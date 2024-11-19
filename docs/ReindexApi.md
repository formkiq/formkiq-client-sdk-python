# formkiq_client.ReindexApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_reindex_document**](ReindexApi.md#add_reindex_document) | **POST** /reindex/documents/{documentId} | Reindex metadata on a document


# **add_reindex_document**
> AddResponse add_reindex_document(document_id, add_reindex_document_request, site_id=site_id)

Reindex metadata on a document

The API allows for the reindexing of a document's metadata determined by the target.  ATTRIBUTE target will regenerate the composite keys for a document based on the Classification / SiteSchema

### Example


```python
import formkiq_client
from formkiq_client.models.add_reindex_document_request import AddReindexDocumentRequest
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
    api_instance = formkiq_client.ReindexApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_reindex_document_request = formkiq_client.AddReindexDocumentRequest() # AddReindexDocumentRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Reindex metadata on a document
        api_response = api_instance.add_reindex_document(document_id, add_reindex_document_request, site_id=site_id)
        print("The response of ReindexApi->add_reindex_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReindexApi->add_reindex_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_reindex_document_request** | [**AddReindexDocumentRequest**](AddReindexDocumentRequest.md)|  | 
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

