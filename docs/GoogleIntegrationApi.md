# formkiq_client.GoogleIntegrationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_google_document_export**](GoogleIntegrationApi.md#add_google_document_export) | **POST** /integrations/google/drive/documents/{documentId}/export | Add Google Document Export


# **add_google_document_export**
> AddGoogleDocumentExportResponse add_google_document_export(document_id, add_google_document_export_request, site_id=site_id)

Add Google Document Export

Exports a Google Document; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_google_document_export_request import AddGoogleDocumentExportRequest
from formkiq_client.models.add_google_document_export_response import AddGoogleDocumentExportResponse
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
    api_instance = formkiq_client.GoogleIntegrationApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_google_document_export_request = formkiq_client.AddGoogleDocumentExportRequest() # AddGoogleDocumentExportRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add Google Document Export
        api_response = api_instance.add_google_document_export(document_id, add_google_document_export_request, site_id=site_id)
        print("The response of GoogleIntegrationApi->add_google_document_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleIntegrationApi->add_google_document_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_google_document_export_request** | [**AddGoogleDocumentExportRequest**](AddGoogleDocumentExportRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddGoogleDocumentExportResponse**](AddGoogleDocumentExportResponse.md)

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

