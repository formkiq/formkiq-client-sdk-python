# openapi_client.DocumentDataClassificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document_data_classification**](DocumentDataClassificationApi.md#get_document_data_classification) | **GET** /documents/{documentId}/dataClassification | Get document&#39;s data classification
[**set_document_data_classification**](DocumentDataClassificationApi.md#set_document_data_classification) | **PUT** /documents/{documentId}/dataClassification | Set document&#39;s data classification


# **get_document_data_classification**
> GetDocumentDataClassificationResponse get_document_data_classification(document_id, site_id=site_id, limit=limit, next=next)

Get document's data classification

Retrieve an document's data classification; available as an Add-On Module

### Example


```python
import openapi_client
from openapi_client.models.get_document_data_classification_response import GetDocumentDataClassificationResponse
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
    api_instance = openapi_client.DocumentDataClassificationApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document's data classification
        api_response = api_instance.get_document_data_classification(document_id, site_id=site_id, limit=limit, next=next)
        print("The response of DocumentDataClassificationApi->get_document_data_classification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentDataClassificationApi->get_document_data_classification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetDocumentDataClassificationResponse**](GetDocumentDataClassificationResponse.md)

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

# **set_document_data_classification**
> SetDocumentDataClassificationResponse set_document_data_classification(document_id, site_id=site_id, set_document_data_classification_request=set_document_data_classification_request)

Set document's data classification

Generate Data Classfication attributes within a document; available as an Add-On Module

### Example


```python
import openapi_client
from openapi_client.models.set_document_data_classification_request import SetDocumentDataClassificationRequest
from openapi_client.models.set_document_data_classification_response import SetDocumentDataClassificationResponse
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
    api_instance = openapi_client.DocumentDataClassificationApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    set_document_data_classification_request = openapi_client.SetDocumentDataClassificationRequest() # SetDocumentDataClassificationRequest |  (optional)

    try:
        # Set document's data classification
        api_response = api_instance.set_document_data_classification(document_id, site_id=site_id, set_document_data_classification_request=set_document_data_classification_request)
        print("The response of DocumentDataClassificationApi->set_document_data_classification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentDataClassificationApi->set_document_data_classification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **set_document_data_classification_request** | [**SetDocumentDataClassificationRequest**](SetDocumentDataClassificationRequest.md)|  | [optional] 

### Return type

[**SetDocumentDataClassificationResponse**](SetDocumentDataClassificationResponse.md)

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

