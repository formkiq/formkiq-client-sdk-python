# formkiq_client.CaseManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_case**](CaseManagementApi.md#add_case) | **POST** /cases | Add New Case
[**delete_case**](CaseManagementApi.md#delete_case) | **DELETE** /cases/{caseId} | Delete Case
[**delete_case_document**](CaseManagementApi.md#delete_case_document) | **DELETE** /cases/{caseId}/documents/{documentId} | Delete Document from Case
[**delete_nigo**](CaseManagementApi.md#delete_nigo) | **DELETE** /cases/{caseId}/nigos/{nigoId} | Delete Nigo
[**delete_nigo_document**](CaseManagementApi.md#delete_nigo_document) | **DELETE** /cases/{caseId}/nigos/{nigoId}/documents/{documentId} | Delete Document from Nigo
[**delete_task**](CaseManagementApi.md#delete_task) | **DELETE** /cases/{caseId}/tasks/{taskId} | Delete Task
[**delete_task_document**](CaseManagementApi.md#delete_task_document) | **DELETE** /cases/{caseId}/tasks/{taskId}/documents/{documentId} | Delete Document from Task
[**get_case**](CaseManagementApi.md#get_case) | **GET** /cases/{caseId} | Get Case details
[**get_case_documents**](CaseManagementApi.md#get_case_documents) | **GET** /cases/{caseId}/documents | Get list of document in a case
[**get_case_nigo**](CaseManagementApi.md#get_case_nigo) | **GET** /cases/{caseId}/nigos/{nigoId} | Get nigo in a case
[**get_case_nigos**](CaseManagementApi.md#get_case_nigos) | **GET** /cases/{caseId}/nigos | Get list of Nigos in a case
[**get_case_task**](CaseManagementApi.md#get_case_task) | **GET** /cases/{caseId}/tasks/{taskId} | Get task in a case
[**get_case_tasks**](CaseManagementApi.md#get_case_tasks) | **GET** /cases/{caseId}/tasks | Get list of tasks in a case
[**get_cases**](CaseManagementApi.md#get_cases) | **GET** /cases | Get Case listing
[**get_nigo_documents**](CaseManagementApi.md#get_nigo_documents) | **GET** /cases/{caseId}/nigos/{nigoId}/documents | Get list of document in a task
[**get_task_documents**](CaseManagementApi.md#get_task_documents) | **GET** /cases/{caseId}/tasks/{taskId}/documents | Get list of document in a task
[**update_case**](CaseManagementApi.md#update_case) | **PATCH** /cases/{caseId} | Update existing Case
[**update_nigo**](CaseManagementApi.md#update_nigo) | **PATCH** /cases/{caseId}/nigos/{nigoId} | Update existing Nigo
[**update_task**](CaseManagementApi.md#update_task) | **PATCH** /cases/{caseId}/tasks/{taskId} | Update existing Task


# **add_case**
> AddCaseResponse add_case(add_case_request, site_id=site_id)

Add New Case

Adds new case; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.add_case_request import AddCaseRequest
from formkiq_client.models.add_case_response import AddCaseResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    add_case_request = formkiq_client.AddCaseRequest() # AddCaseRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add New Case
        api_response = api_instance.add_case(add_case_request, site_id=site_id)
        print("The response of CaseManagementApi->add_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->add_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_case_request** | [**AddCaseRequest**](AddCaseRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddCaseResponse**](AddCaseResponse.md)

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

# **delete_case**
> DeleteCaseResponse delete_case(case_id, site_id=site_id)

Delete Case

Delete Case

### Example


```python
import formkiq_client
from formkiq_client.models.delete_case_response import DeleteCaseResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete Case
        api_response = api_instance.delete_case(case_id, site_id=site_id)
        print("The response of CaseManagementApi->delete_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->delete_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteCaseResponse**](DeleteCaseResponse.md)

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

# **delete_case_document**
> DeleteCaseDocumentResponse delete_case_document(case_id, document_id, site_id=site_id)

Delete Document from Case

Delete Document from Case

### Example


```python
import formkiq_client
from formkiq_client.models.delete_case_document_response import DeleteCaseDocumentResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete Document from Case
        api_response = api_instance.delete_case_document(case_id, document_id, site_id=site_id)
        print("The response of CaseManagementApi->delete_case_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->delete_case_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteCaseDocumentResponse**](DeleteCaseDocumentResponse.md)

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

# **delete_nigo**
> DeleteCaseNigoResponse delete_nigo(case_id, nigo_id, site_id=site_id)

Delete Nigo

Delete Nigo

### Example


```python
import formkiq_client
from formkiq_client.models.delete_case_nigo_response import DeleteCaseNigoResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    nigo_id = 'nigo_id_example' # str | Nigo Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete Nigo
        api_response = api_instance.delete_nigo(case_id, nigo_id, site_id=site_id)
        print("The response of CaseManagementApi->delete_nigo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->delete_nigo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **nigo_id** | **str**| Nigo Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteCaseNigoResponse**](DeleteCaseNigoResponse.md)

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

# **delete_nigo_document**
> DeleteCaseNigoDocumentResponse delete_nigo_document(case_id, nigo_id, document_id, site_id=site_id)

Delete Document from Nigo

Delete Document from Nigo

### Example


```python
import formkiq_client
from formkiq_client.models.delete_case_nigo_document_response import DeleteCaseNigoDocumentResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    nigo_id = 'nigo_id_example' # str | Nigo Identifier
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete Document from Nigo
        api_response = api_instance.delete_nigo_document(case_id, nigo_id, document_id, site_id=site_id)
        print("The response of CaseManagementApi->delete_nigo_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->delete_nigo_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **nigo_id** | **str**| Nigo Identifier | 
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteCaseNigoDocumentResponse**](DeleteCaseNigoDocumentResponse.md)

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

# **delete_task**
> DeleteCaseTaskResponse delete_task(case_id, task_id, site_id=site_id)

Delete Task

Delete Task

### Example


```python
import formkiq_client
from formkiq_client.models.delete_case_task_response import DeleteCaseTaskResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    task_id = 'task_id_example' # str | Task Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete Task
        api_response = api_instance.delete_task(case_id, task_id, site_id=site_id)
        print("The response of CaseManagementApi->delete_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->delete_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **task_id** | **str**| Task Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteCaseTaskResponse**](DeleteCaseTaskResponse.md)

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

# **delete_task_document**
> DeleteCaseTaskDocumentResponse delete_task_document(case_id, task_id, document_id, site_id=site_id)

Delete Document from Task

Delete Document from Task

### Example


```python
import formkiq_client
from formkiq_client.models.delete_case_task_document_response import DeleteCaseTaskDocumentResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    task_id = 'task_id_example' # str | Task Identifier
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete Document from Task
        api_response = api_instance.delete_task_document(case_id, task_id, document_id, site_id=site_id)
        print("The response of CaseManagementApi->delete_task_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->delete_task_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **task_id** | **str**| Task Identifier | 
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteCaseTaskDocumentResponse**](DeleteCaseTaskDocumentResponse.md)

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

# **get_case**
> GetCaseResponse get_case(case_id, site_id=site_id)

Get Case details

Returns a Case; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_case_response import GetCaseResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get Case details
        api_response = api_instance.get_case(case_id, site_id=site_id)
        print("The response of CaseManagementApi->get_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->get_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetCaseResponse**](GetCaseResponse.md)

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

# **get_case_documents**
> GetCaseDocumentsResponse get_case_documents(case_id, site_id=site_id, next=next, limit=limit)

Get list of document in a case

Returns documents in a Case; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_case_documents_response import GetCaseDocumentsResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get list of document in a case
        api_response = api_instance.get_case_documents(case_id, site_id=site_id, next=next, limit=limit)
        print("The response of CaseManagementApi->get_case_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->get_case_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetCaseDocumentsResponse**](GetCaseDocumentsResponse.md)

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

# **get_case_nigo**
> GetCaseNigoResponse get_case_nigo(case_id, nigo_id, site_id=site_id)

Get nigo in a case

Returns a Nigo in Case; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_case_nigo_response import GetCaseNigoResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    nigo_id = 'nigo_id_example' # str | Nigo Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get nigo in a case
        api_response = api_instance.get_case_nigo(case_id, nigo_id, site_id=site_id)
        print("The response of CaseManagementApi->get_case_nigo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->get_case_nigo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **nigo_id** | **str**| Nigo Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetCaseNigoResponse**](GetCaseNigoResponse.md)

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

# **get_case_nigos**
> GetCaseNigosResponse get_case_nigos(case_id, site_id=site_id, next=next, limit=limit)

Get list of Nigos in a case

Returns a Nigos of Case; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_case_nigos_response import GetCaseNigosResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get list of Nigos in a case
        api_response = api_instance.get_case_nigos(case_id, site_id=site_id, next=next, limit=limit)
        print("The response of CaseManagementApi->get_case_nigos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->get_case_nigos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetCaseNigosResponse**](GetCaseNigosResponse.md)

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

# **get_case_task**
> GetCaseTaskResponse get_case_task(case_id, task_id, site_id=site_id)

Get task in a case

Returns a Task in Case; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_case_task_response import GetCaseTaskResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    task_id = 'task_id_example' # str | Task Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get task in a case
        api_response = api_instance.get_case_task(case_id, task_id, site_id=site_id)
        print("The response of CaseManagementApi->get_case_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->get_case_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **task_id** | **str**| Task Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetCaseTaskResponse**](GetCaseTaskResponse.md)

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

# **get_case_tasks**
> GetCaseTasksResponse get_case_tasks(case_id, site_id=site_id, next=next, limit=limit)

Get list of tasks in a case

Returns a Case; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_case_tasks_response import GetCaseTasksResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get list of tasks in a case
        api_response = api_instance.get_case_tasks(case_id, site_id=site_id, next=next, limit=limit)
        print("The response of CaseManagementApi->get_case_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->get_case_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetCaseTasksResponse**](GetCaseTasksResponse.md)

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

# **get_cases**
> GetCasesResponse get_cases(site_id=site_id, next=next, limit=limit)

Get Case listing

Returns a list of the Cases; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_cases_response import GetCasesResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get Case listing
        api_response = api_instance.get_cases(site_id=site_id, next=next, limit=limit)
        print("The response of CaseManagementApi->get_cases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->get_cases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetCasesResponse**](GetCasesResponse.md)

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

# **get_nigo_documents**
> GetCaseDocumentsResponse get_nigo_documents(case_id, nigo_id, site_id=site_id, next=next, limit=limit)

Get list of document in a task

Returns a list documents in a Case; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_case_documents_response import GetCaseDocumentsResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    nigo_id = 'nigo_id_example' # str | Nigo Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get list of document in a task
        api_response = api_instance.get_nigo_documents(case_id, nigo_id, site_id=site_id, next=next, limit=limit)
        print("The response of CaseManagementApi->get_nigo_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->get_nigo_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **nigo_id** | **str**| Nigo Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetCaseDocumentsResponse**](GetCaseDocumentsResponse.md)

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

# **get_task_documents**
> GetCaseDocumentsResponse get_task_documents(case_id, task_id, site_id=site_id, next=next, limit=limit)

Get list of document in a task

Returns a list documents in a Case; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_case_documents_response import GetCaseDocumentsResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    task_id = 'task_id_example' # str | Task Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get list of document in a task
        api_response = api_instance.get_task_documents(case_id, task_id, site_id=site_id, next=next, limit=limit)
        print("The response of CaseManagementApi->get_task_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->get_task_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **task_id** | **str**| Task Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetCaseDocumentsResponse**](GetCaseDocumentsResponse.md)

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

# **update_case**
> UpdateCaseResponse update_case(case_id, update_case_request, site_id=site_id)

Update existing Case

Updates existing case; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.update_case_request import UpdateCaseRequest
from formkiq_client.models.update_case_response import UpdateCaseResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    update_case_request = formkiq_client.UpdateCaseRequest() # UpdateCaseRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Update existing Case
        api_response = api_instance.update_case(case_id, update_case_request, site_id=site_id)
        print("The response of CaseManagementApi->update_case:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->update_case: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **update_case_request** | [**UpdateCaseRequest**](UpdateCaseRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**UpdateCaseResponse**](UpdateCaseResponse.md)

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

# **update_nigo**
> UpdateNigoResponse update_nigo(case_id, nigo_id, update_nigo_request, site_id=site_id)

Update existing Nigo

Updates existing nigo; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.update_nigo_request import UpdateNigoRequest
from formkiq_client.models.update_nigo_response import UpdateNigoResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    nigo_id = 'nigo_id_example' # str | Nigo Identifier
    update_nigo_request = formkiq_client.UpdateNigoRequest() # UpdateNigoRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Update existing Nigo
        api_response = api_instance.update_nigo(case_id, nigo_id, update_nigo_request, site_id=site_id)
        print("The response of CaseManagementApi->update_nigo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->update_nigo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **nigo_id** | **str**| Nigo Identifier | 
 **update_nigo_request** | [**UpdateNigoRequest**](UpdateNigoRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**UpdateNigoResponse**](UpdateNigoResponse.md)

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

# **update_task**
> UpdateTaskResponse update_task(case_id, task_id, update_task_request, site_id=site_id)

Update existing Task

Updates existing task; ONLY available with FormKiQ Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.update_task_request import UpdateTaskRequest
from formkiq_client.models.update_task_response import UpdateTaskResponse
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
    api_instance = formkiq_client.CaseManagementApi(api_client)
    case_id = 'case_id_example' # str | Case Identifier
    task_id = 'task_id_example' # str | Task Identifier
    update_task_request = formkiq_client.UpdateTaskRequest() # UpdateTaskRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Update existing Task
        api_response = api_instance.update_task(case_id, task_id, update_task_request, site_id=site_id)
        print("The response of CaseManagementApi->update_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaseManagementApi->update_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **case_id** | **str**| Case Identifier | 
 **task_id** | **str**| Task Identifier | 
 **update_task_request** | [**UpdateTaskRequest**](UpdateTaskRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**UpdateTaskResponse**](UpdateTaskResponse.md)

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

