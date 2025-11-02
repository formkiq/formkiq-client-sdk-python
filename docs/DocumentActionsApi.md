# openapi_client.DocumentActionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_actions**](DocumentActionsApi.md#add_document_actions) | **POST** /documents/{documentId}/actions | Add document action
[**add_document_retry_action**](DocumentActionsApi.md#add_document_retry_action) | **POST** /documents/{documentId}/actions/retry | Retries failed document action(s)
[**get_document_actions**](DocumentActionsApi.md#get_document_actions) | **GET** /documents/{documentId}/actions | Get document actions


# **add_document_actions**
> AddDocumentActionsResponse add_document_actions(document_id, site_id=site_id, add_document_actions_request=add_document_actions_request)

Add document action

Add one or more actions to a document; this appends actions and does not replace previous actions

Each action type supports a different set of parameters as shown in the table below:

### Action Parameters

| ActionType | Parameter | Description | Example |
| -------- | ------- | ------- | ------- |
| OCR  | ocrParseTypes | Ocr Parsing strategy to use | TEXT, FORMS, TABLES, QUERIES (requires 'ocrTextractQueries') |
| OCR  | ocrTextractQueries | Required for "QUERIES", questions to ask Textract |
| OCR | ocrEngine     | Ocr Engine to use | tesseract or textract |
| OCR | ocrOutputType     | Convert OCR result to an Output format (textract table only) | true |
| OCR | ocrNumberOfPages  | Number of pages to OCR (from start) | -1 |
| OCR    | addPdfDetectedCharactersAsText | PDF Documents convert images to text | true or false |
| DATA_CLASSIFICATION | llmPromptEntityName | LLM Prompt Entity Name |
| FULLTEXT    | characterMax    | Maximum number of characters to add to Fulltext destination | -1 |
| DOCUMENTTAGGING    | engine    | Tagging Engine to use | chatgpt |
| DOCUMENTTAGGING    | tags    | Comma-deliminted list of keywords | author,title,description |
| WEBHOOK    | url    | Webhook URL | https://yourdomain.com/webhook-endpoint |
| NOTIFICATION    | notificationType | Type of Notification | email |
| NOTIFICATION    | notificationToCc    | Notification Carbon Copy | email@yourdomain.com |
| NOTIFICATION    | notificationToBcc    | Notification Blind Carbon Copy | email@yourdomain.com |
| NOTIFICATION    | notificationSubject    | Notification Subject | Email Subject |
| NOTIFICATION    | notificationText    | Notification as Text | Email Text |
| NOTIFICATION    | notificationHtml    | Notification as Html | Email HTML Text |
| QUEUE    | queueId    | Id of Queue | |
| IDP    | mappingId    | Id of Mapping | |
| EVENTBRIDGE    | eventBusName    | The name or ARN of the Amazon EventBridge to receive the event. | |
| RESIZE    | width    | The width of the image to resize (or 'auto'). | |
| RESIZE    | height    | The height of the image to resize (or 'auto'). | |
| RESIZE    | outputType    | The output type of the image (optional). | |
| RESIZE    | path    | The path to use when creating resized document (optional). | |

### Example


```python
import openapi_client
from openapi_client.models.add_document_actions_request import AddDocumentActionsRequest
from openapi_client.models.add_document_actions_response import AddDocumentActionsResponse
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
    api_instance = openapi_client.DocumentActionsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    add_document_actions_request = openapi_client.AddDocumentActionsRequest() # AddDocumentActionsRequest |  (optional)

    try:
        # Add document action
        api_response = api_instance.add_document_actions(document_id, site_id=site_id, add_document_actions_request=add_document_actions_request)
        print("The response of DocumentActionsApi->add_document_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentActionsApi->add_document_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **add_document_actions_request** | [**AddDocumentActionsRequest**](AddDocumentActionsRequest.md)|  | [optional] 

### Return type

[**AddDocumentActionsResponse**](AddDocumentActionsResponse.md)

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

# **add_document_retry_action**
> AddDocumentActionsRetryResponse add_document_retry_action(document_id, site_id=site_id)

Retries failed document action(s)

Retries all failed document action(s). Failed action status changes to "FAILED_RETRY" and a new "PENDING" action is created.

### Example


```python
import openapi_client
from openapi_client.models.add_document_actions_retry_response import AddDocumentActionsRetryResponse
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
    api_instance = openapi_client.DocumentActionsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Retries failed document action(s)
        api_response = api_instance.add_document_retry_action(document_id, site_id=site_id)
        print("The response of DocumentActionsApi->add_document_retry_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentActionsApi->add_document_retry_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddDocumentActionsRetryResponse**](AddDocumentActionsRetryResponse.md)

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

# **get_document_actions**
> GetDocumentActionsResponse get_document_actions(document_id, site_id=site_id, limit=limit, share_key=share_key, next=next)

Get document actions

Get document actions and their status

### Example


```python
import openapi_client
from openapi_client.models.get_document_actions_response import GetDocumentActionsResponse
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
    api_instance = openapi_client.DocumentActionsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    share_key = 'share_key_example' # str | Share Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document actions
        api_response = api_instance.get_document_actions(document_id, site_id=site_id, limit=limit, share_key=share_key, next=next)
        print("The response of DocumentActionsApi->get_document_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentActionsApi->get_document_actions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **share_key** | **str**| Share Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetDocumentActionsResponse**](GetDocumentActionsResponse.md)

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

