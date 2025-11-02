# openapi_client.DocumentGenerationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_generate**](DocumentGenerationApi.md#add_document_generate) | **POST** /documents/{documentId}/generate | Add Document Generate


# **add_document_generate**
> AddDocumentGenerateResponse add_document_generate(document_id, add_document_generate_request, site_id=site_id)

Add Document Generate

Generates a new document using a specified template file and data sources. This operation allows users to merge data from multiple documents into a template to create a new document in the desired output format (e.g., DOCX).

By Default data source must include a `data` object, which contains key-value pairs that will be merged into the template. The value can be any valid JSON object. { "data":{}}. The data path can be adjusted via the "dataRoot" field.

; available as an Add-On Module

### Example


```python
import openapi_client
from openapi_client.models.add_document_generate_request import AddDocumentGenerateRequest
from openapi_client.models.add_document_generate_response import AddDocumentGenerateResponse
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
    api_instance = openapi_client.DocumentGenerationApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_document_generate_request = openapi_client.AddDocumentGenerateRequest() # AddDocumentGenerateRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add Document Generate
        api_response = api_instance.add_document_generate(document_id, add_document_generate_request, site_id=site_id)
        print("The response of DocumentGenerationApi->add_document_generate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentGenerationApi->add_document_generate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_document_generate_request** | [**AddDocumentGenerateRequest**](AddDocumentGenerateRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddDocumentGenerateResponse**](AddDocumentGenerateResponse.md)

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

