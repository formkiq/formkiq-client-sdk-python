# formkiq_client.DocumentWorkflowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_workflow**](DocumentWorkflowsApi.md#add_document_workflow) | **POST** /documents/{documentId}/workflows | Add document workflow
[**add_document_workflow_decisions**](DocumentWorkflowsApi.md#add_document_workflow_decisions) | **POST** /documents/{documentId}/workflow/{workflowId}/decisions | Approve/Reject document in approval queue
[**add_queue**](DocumentWorkflowsApi.md#add_queue) | **POST** /queues | Add queue
[**add_workflow**](DocumentWorkflowsApi.md#add_workflow) | **POST** /workflows | Add workflow
[**delete_queue**](DocumentWorkflowsApi.md#delete_queue) | **DELETE** /queues/{queueId} | Delete queue
[**delete_workflow**](DocumentWorkflowsApi.md#delete_workflow) | **DELETE** /workflows/{workflowId} | Delete workflow
[**get_document_workflow**](DocumentWorkflowsApi.md#get_document_workflow) | **GET** /documents/{documentId}/workflows/{workflowId} | Get document workflow
[**get_document_workflows**](DocumentWorkflowsApi.md#get_document_workflows) | **GET** /documents/{documentId}/workflows | Get document workflows
[**get_queue**](DocumentWorkflowsApi.md#get_queue) | **GET** /queues/{queueId} | Get queue
[**get_queues**](DocumentWorkflowsApi.md#get_queues) | **GET** /queues | Get queues
[**get_workflow**](DocumentWorkflowsApi.md#get_workflow) | **GET** /workflows/{workflowId} | Get workflow
[**get_workflow_documents**](DocumentWorkflowsApi.md#get_workflow_documents) | **GET** /workflows/{workflowId}/documents | Get list of documents in workflow
[**get_workflow_queue_documents**](DocumentWorkflowsApi.md#get_workflow_queue_documents) | **GET** /queues/{queueId}/documents | Get list of documents in queue
[**get_workflows**](DocumentWorkflowsApi.md#get_workflows) | **GET** /workflows | Get workflows
[**set_workflow**](DocumentWorkflowsApi.md#set_workflow) | **PUT** /workflows/{workflowId} | Set workflow
[**update_workflow**](DocumentWorkflowsApi.md#update_workflow) | **PATCH** /workflows/{workflowId} | Update workflow


# **add_document_workflow**
> AddDocumentWorkflowResponse add_document_workflow(document_id, add_document_workflow_request, site_id=site_id)

Add document workflow

Creates a document workflow; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_workflow_request import AddDocumentWorkflowRequest
from formkiq_client.models.add_document_workflow_response import AddDocumentWorkflowResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_document_workflow_request = formkiq_client.AddDocumentWorkflowRequest() # AddDocumentWorkflowRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add document workflow
        api_response = api_instance.add_document_workflow(document_id, add_document_workflow_request, site_id=site_id)
        print("The response of DocumentWorkflowsApi->add_document_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->add_document_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_document_workflow_request** | [**AddDocumentWorkflowRequest**](AddDocumentWorkflowRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddDocumentWorkflowResponse**](AddDocumentWorkflowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 BAD REQUEST |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_document_workflow_decisions**
> AddDocumentWorkflowDecisionsResponse add_document_workflow_decisions(document_id, workflow_id, add_document_workflow_decisions_request, site_id=site_id)

Approve/Reject document in approval queue

Approve/Reject document in approval queue; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_workflow_decisions_request import AddDocumentWorkflowDecisionsRequest
from formkiq_client.models.add_document_workflow_decisions_response import AddDocumentWorkflowDecisionsResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    workflow_id = 'workflow_id_example' # str | Workflow Identifier
    add_document_workflow_decisions_request = formkiq_client.AddDocumentWorkflowDecisionsRequest() # AddDocumentWorkflowDecisionsRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Approve/Reject document in approval queue
        api_response = api_instance.add_document_workflow_decisions(document_id, workflow_id, add_document_workflow_decisions_request, site_id=site_id)
        print("The response of DocumentWorkflowsApi->add_document_workflow_decisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->add_document_workflow_decisions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **workflow_id** | **str**| Workflow Identifier | 
 **add_document_workflow_decisions_request** | [**AddDocumentWorkflowDecisionsRequest**](AddDocumentWorkflowDecisionsRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddDocumentWorkflowDecisionsResponse**](AddDocumentWorkflowDecisionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 BAD REQUEST |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_queue**
> AddQueueResponse add_queue(add_queue_request, site_id=site_id)

Add queue

Creates a new Queue; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_queue_request import AddQueueRequest
from formkiq_client.models.add_queue_response import AddQueueResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    add_queue_request = formkiq_client.AddQueueRequest() # AddQueueRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add queue
        api_response = api_instance.add_queue(add_queue_request, site_id=site_id)
        print("The response of DocumentWorkflowsApi->add_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->add_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_queue_request** | [**AddQueueRequest**](AddQueueRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddQueueResponse**](AddQueueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 BAD REQUEST |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_workflow**
> AddWorkflowResponse add_workflow(add_workflow_request, site_id=site_id)

Add workflow

Creates a new Workflow; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_workflow_request import AddWorkflowRequest
from formkiq_client.models.add_workflow_response import AddWorkflowResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    add_workflow_request = formkiq_client.AddWorkflowRequest() # AddWorkflowRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add workflow
        api_response = api_instance.add_workflow(add_workflow_request, site_id=site_id)
        print("The response of DocumentWorkflowsApi->add_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->add_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_workflow_request** | [**AddWorkflowRequest**](AddWorkflowRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddWorkflowResponse**](AddWorkflowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 BAD REQUEST |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_queue**
> DeleteQueueResponse delete_queue(queue_id, site_id=site_id)

Delete queue

Delete a Queue; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.delete_queue_response import DeleteQueueResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    queue_id = 'queue_id_example' # str | Queue Id
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete queue
        api_response = api_instance.delete_queue(queue_id, site_id=site_id)
        print("The response of DocumentWorkflowsApi->delete_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->delete_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_id** | **str**| Queue Id | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteQueueResponse**](DeleteQueueResponse.md)

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

# **delete_workflow**
> DeleteWorkflowResponse delete_workflow(workflow_id, site_id=site_id)

Delete workflow

Delete a Workflow; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.delete_workflow_response import DeleteWorkflowResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    workflow_id = 'workflow_id_example' # str | Workflow Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete workflow
        api_response = api_instance.delete_workflow(workflow_id, site_id=site_id)
        print("The response of DocumentWorkflowsApi->delete_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->delete_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| Workflow Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteWorkflowResponse**](DeleteWorkflowResponse.md)

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

# **get_document_workflow**
> GetDocumentWorkflowResponse get_document_workflow(document_id, workflow_id, site_id=site_id)

Get document workflow

Gets a document workflow; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_workflow_response import GetDocumentWorkflowResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    workflow_id = 'workflow_id_example' # str | Workflow Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get document workflow
        api_response = api_instance.get_document_workflow(document_id, workflow_id, site_id=site_id)
        print("The response of DocumentWorkflowsApi->get_document_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->get_document_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **workflow_id** | **str**| Workflow Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetDocumentWorkflowResponse**](GetDocumentWorkflowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 BAD REQUEST |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_workflows**
> GetDocumentWorkflowsResponse get_document_workflows(document_id, site_id=site_id)

Get document workflows

Gets a document workflows; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_workflows_response import GetDocumentWorkflowsResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get document workflows
        api_response = api_instance.get_document_workflows(document_id, site_id=site_id)
        print("The response of DocumentWorkflowsApi->get_document_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->get_document_workflows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetDocumentWorkflowsResponse**](GetDocumentWorkflowsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 BAD REQUEST |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queue**
> GetQueueResponse get_queue(queue_id, site_id=site_id)

Get queue

Get a queue; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_queue_response import GetQueueResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    queue_id = 'queue_id_example' # str | Queue Id
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get queue
        api_response = api_instance.get_queue(queue_id, site_id=site_id)
        print("The response of DocumentWorkflowsApi->get_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->get_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_id** | **str**| Queue Id | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetQueueResponse**](GetQueueResponse.md)

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

# **get_queues**
> GetQueuesResponse get_queues(site_id=site_id, next=next, limit=limit)

Get queues

Get a listing of queues; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_queues_response import GetQueuesResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get queues
        api_response = api_instance.get_queues(site_id=site_id, next=next, limit=limit)
        print("The response of DocumentWorkflowsApi->get_queues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->get_queues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetQueuesResponse**](GetQueuesResponse.md)

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

# **get_workflow**
> GetWorkflowResponse get_workflow(workflow_id, site_id=site_id)

Get workflow

Get a workflow; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_workflow_response import GetWorkflowResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    workflow_id = 'workflow_id_example' # str | Workflow Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get workflow
        api_response = api_instance.get_workflow(workflow_id, site_id=site_id)
        print("The response of DocumentWorkflowsApi->get_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->get_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| Workflow Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetWorkflowResponse**](GetWorkflowResponse.md)

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

# **get_workflow_documents**
> GetWorkflowDocumentsResponse get_workflow_documents(workflow_id, site_id=site_id, limit=limit, next=next)

Get list of documents in workflow

List documents in Workflow; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_workflow_documents_response import GetWorkflowDocumentsResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    workflow_id = 'workflow_id_example' # str | Workflow Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get list of documents in workflow
        api_response = api_instance.get_workflow_documents(workflow_id, site_id=site_id, limit=limit, next=next)
        print("The response of DocumentWorkflowsApi->get_workflow_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->get_workflow_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| Workflow Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetWorkflowDocumentsResponse**](GetWorkflowDocumentsResponse.md)

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

# **get_workflow_queue_documents**
> GetWorkflowQueueDocumentsResponse get_workflow_queue_documents(queue_id, site_id=site_id, limit=limit, next=next)

Get list of documents in queue

List documents in Workflow Queue; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_workflow_queue_documents_response import GetWorkflowQueueDocumentsResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    queue_id = 'queue_id_example' # str | Queue Id
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get list of documents in queue
        api_response = api_instance.get_workflow_queue_documents(queue_id, site_id=site_id, limit=limit, next=next)
        print("The response of DocumentWorkflowsApi->get_workflow_queue_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->get_workflow_queue_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **queue_id** | **str**| Queue Id | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetWorkflowQueueDocumentsResponse**](GetWorkflowQueueDocumentsResponse.md)

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

# **get_workflows**
> GetWorkflowsResponse get_workflows(site_id=site_id, next=next, limit=limit, status=status)

Get workflows

Get a listing of workflows; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_workflows_response import GetWorkflowsResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    status = 'status_example' # str | Filters Status (optional)

    try:
        # Get workflows
        api_response = api_instance.get_workflows(site_id=site_id, next=next, limit=limit, status=status)
        print("The response of DocumentWorkflowsApi->get_workflows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->get_workflows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **status** | **str**| Filters Status | [optional] 

### Return type

[**GetWorkflowsResponse**](GetWorkflowsResponse.md)

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

# **set_workflow**
> SetWorkflowResponse set_workflow(workflow_id, set_workflow_request, site_id=site_id)

Set workflow

Set a Workflow details; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.set_workflow_request import SetWorkflowRequest
from formkiq_client.models.set_workflow_response import SetWorkflowResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    workflow_id = 'workflow_id_example' # str | Workflow Identifier
    set_workflow_request = formkiq_client.SetWorkflowRequest() # SetWorkflowRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Set workflow
        api_response = api_instance.set_workflow(workflow_id, set_workflow_request, site_id=site_id)
        print("The response of DocumentWorkflowsApi->set_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->set_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| Workflow Identifier | 
 **set_workflow_request** | [**SetWorkflowRequest**](SetWorkflowRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**SetWorkflowResponse**](SetWorkflowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 20) OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 BAD REQUEST |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workflow**
> UpdateWorkflowResponse update_workflow(workflow_id, update_workflow_request, site_id=site_id)

Update workflow

Update a Workflow details; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.update_workflow_request import UpdateWorkflowRequest
from formkiq_client.models.update_workflow_response import UpdateWorkflowResponse
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
    api_instance = formkiq_client.DocumentWorkflowsApi(api_client)
    workflow_id = 'workflow_id_example' # str | Workflow Identifier
    update_workflow_request = formkiq_client.UpdateWorkflowRequest() # UpdateWorkflowRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Update workflow
        api_response = api_instance.update_workflow(workflow_id, update_workflow_request, site_id=site_id)
        print("The response of DocumentWorkflowsApi->update_workflow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentWorkflowsApi->update_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_id** | **str**| Workflow Identifier | 
 **update_workflow_request** | [**UpdateWorkflowRequest**](UpdateWorkflowRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**UpdateWorkflowResponse**](UpdateWorkflowResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 20) OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 BAD REQUEST |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

