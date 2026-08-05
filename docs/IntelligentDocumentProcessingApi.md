# formkiq_client.IntelligentDocumentProcessingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_ai_prompt**](IntelligentDocumentProcessingApi.md#add_document_ai_prompt) | **POST** /documents/{documentId}/ai/prompts/{llmPromptEntityName} | Add document AI result from LLM prompt
[**add_document_metadata_extraction_result**](IntelligentDocumentProcessingApi.md#add_document_metadata_extraction_result) | **POST** /documents/{documentId}/metadataExtractionResults/{llmPromptEntityName} | Add document&#39;s metadata extraction result
[**get_all_document_metadata_extraction_results**](IntelligentDocumentProcessingApi.md#get_all_document_metadata_extraction_results) | **GET** /documents/{documentId}/metadataExtractionResults | Get all document&#39;s metadata extraction results
[**get_document_ai_prompt_results**](IntelligentDocumentProcessingApi.md#get_document_ai_prompt_results) | **GET** /documents/{documentId}/ai/prompts/{llmPromptEntityName} | Get document AI results from LLM prompt
[**get_document_ai_prompts_results**](IntelligentDocumentProcessingApi.md#get_document_ai_prompts_results) | **GET** /documents/{documentId}/ai/prompts | Get document AI results from LLM prompts
[**get_document_data_classification**](IntelligentDocumentProcessingApi.md#get_document_data_classification) | **GET** /documents/{documentId}/dataClassification | Get document&#39;s data classification
[**get_document_metadata_extraction_results**](IntelligentDocumentProcessingApi.md#get_document_metadata_extraction_results) | **GET** /documents/{documentId}/metadataExtractionResults/{llmPromptEntityName} | Get document&#39;s metadata extraction results
[**set_document_data_classification**](IntelligentDocumentProcessingApi.md#set_document_data_classification) | **PUT** /documents/{documentId}/dataClassification | Set document&#39;s data classification


# **add_document_ai_prompt**
> AddDocumentAiResponse add_document_ai_prompt(document_id, llm_prompt_entity_name, site_id=site_id, artifact_id=artifact_id, add_document_ai_prompt_request=add_document_ai_prompt_request)

Add document AI result from LLM prompt

Run an LLM prompt against a document; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_ai_prompt_request import AddDocumentAiPromptRequest
from formkiq_client.models.add_document_ai_response import AddDocumentAiResponse
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
    api_instance = formkiq_client.IntelligentDocumentProcessingApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    llm_prompt_entity_name = 'llm_prompt_entity_name_example' # str | LlmPrompt Entity Name
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    add_document_ai_prompt_request = formkiq_client.AddDocumentAiPromptRequest() # AddDocumentAiPromptRequest |  (optional)

    try:
        # Add document AI result from LLM prompt
        api_response = api_instance.add_document_ai_prompt(document_id, llm_prompt_entity_name, site_id=site_id, artifact_id=artifact_id, add_document_ai_prompt_request=add_document_ai_prompt_request)
        print("The response of IntelligentDocumentProcessingApi->add_document_ai_prompt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntelligentDocumentProcessingApi->add_document_ai_prompt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **llm_prompt_entity_name** | **str**| LlmPrompt Entity Name | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
 **add_document_ai_prompt_request** | [**AddDocumentAiPromptRequest**](AddDocumentAiPromptRequest.md)|  | [optional] 

### Return type

[**AddDocumentAiResponse**](AddDocumentAiResponse.md)

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

# **add_document_metadata_extraction_result**
> AddDocumentMetadataExtractionResponse add_document_metadata_extraction_result(document_id, llm_prompt_entity_name, site_id=site_id, artifact_id=artifact_id)

Add document's metadata extraction result

Create a document Metadatq Extraction Result attributes within a document; available as an Add-On Module.
**Deprecated**. This endpoint is no longer recommended.
Please use **`/documents/{documentId}/ai/prompts/{llmPromptEntityName}`** instead.


### Example


```python
import formkiq_client
from formkiq_client.models.add_document_metadata_extraction_response import AddDocumentMetadataExtractionResponse
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
    api_instance = formkiq_client.IntelligentDocumentProcessingApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    llm_prompt_entity_name = 'llm_prompt_entity_name_example' # str | LlmPrompt Entity Name
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)

    try:
        # Add document's metadata extraction result
        api_response = api_instance.add_document_metadata_extraction_result(document_id, llm_prompt_entity_name, site_id=site_id, artifact_id=artifact_id)
        print("The response of IntelligentDocumentProcessingApi->add_document_metadata_extraction_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntelligentDocumentProcessingApi->add_document_metadata_extraction_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **llm_prompt_entity_name** | **str**| LlmPrompt Entity Name | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 

### Return type

[**AddDocumentMetadataExtractionResponse**](AddDocumentMetadataExtractionResponse.md)

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

# **get_all_document_metadata_extraction_results**
> GetDocumentMetadataExtractionResponse get_all_document_metadata_extraction_results(document_id, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)

Get all document's metadata extraction results

Retrieve all document's metadata extraction; available as an Add-On Module.
**Deprecated**. This endpoint is no longer recommended.
Please use **`/documents/{documentId}/ai/prompts/{llmPromptEntityName}`** instead.


### Example


```python
import formkiq_client
from formkiq_client.models.get_document_metadata_extraction_response import GetDocumentMetadataExtractionResponse
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
    api_instance = formkiq_client.IntelligentDocumentProcessingApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get all document's metadata extraction results
        api_response = api_instance.get_all_document_metadata_extraction_results(document_id, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)
        print("The response of IntelligentDocumentProcessingApi->get_all_document_metadata_extraction_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntelligentDocumentProcessingApi->get_all_document_metadata_extraction_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetDocumentMetadataExtractionResponse**](GetDocumentMetadataExtractionResponse.md)

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

# **get_document_ai_prompt_results**
> GetDocumentAiPromptResultsResponse get_document_ai_prompt_results(document_id, llm_prompt_entity_name, site_id=site_id, artifact_id=artifact_id, analysis_category=analysis_category, limit=limit, next=next)

Get document AI results from LLM prompt

Retrieve document AI results from an LLM prompt; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_ai_prompt_results_response import GetDocumentAiPromptResultsResponse
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
    api_instance = formkiq_client.IntelligentDocumentProcessingApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    llm_prompt_entity_name = 'llm_prompt_entity_name_example' # str | LlmPrompt Entity Name
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    analysis_category = 'analysis_category_example' # str | Analysis Category (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document AI results from LLM prompt
        api_response = api_instance.get_document_ai_prompt_results(document_id, llm_prompt_entity_name, site_id=site_id, artifact_id=artifact_id, analysis_category=analysis_category, limit=limit, next=next)
        print("The response of IntelligentDocumentProcessingApi->get_document_ai_prompt_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntelligentDocumentProcessingApi->get_document_ai_prompt_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **llm_prompt_entity_name** | **str**| LlmPrompt Entity Name | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
 **analysis_category** | **str**| Analysis Category | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetDocumentAiPromptResultsResponse**](GetDocumentAiPromptResultsResponse.md)

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

# **get_document_ai_prompts_results**
> GetDocumentAiPromptsResultsResponse get_document_ai_prompts_results(document_id, site_id=site_id, artifact_id=artifact_id, analysis_category=analysis_category, limit=limit, next=next)

Get document AI results from LLM prompts

Retrieve document AI results from LLM prompts; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_ai_prompts_results_response import GetDocumentAiPromptsResultsResponse
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
    api_instance = formkiq_client.IntelligentDocumentProcessingApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    analysis_category = 'analysis_category_example' # str | Analysis Category (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document AI results from LLM prompts
        api_response = api_instance.get_document_ai_prompts_results(document_id, site_id=site_id, artifact_id=artifact_id, analysis_category=analysis_category, limit=limit, next=next)
        print("The response of IntelligentDocumentProcessingApi->get_document_ai_prompts_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntelligentDocumentProcessingApi->get_document_ai_prompts_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
 **analysis_category** | **str**| Analysis Category | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetDocumentAiPromptsResultsResponse**](GetDocumentAiPromptsResultsResponse.md)

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

# **get_document_data_classification**
> GetDocumentDataClassificationResponse get_document_data_classification(document_id, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)

Get document's data classification

Retrieve an document's data classification; available as an Add-On Module.
**Deprecated**. This endpoint is no longer recommended.
Please use **`/documents/{documentId}/ai/prompts/{llmPromptEntityName}`** instead.


### Example


```python
import formkiq_client
from formkiq_client.models.get_document_data_classification_response import GetDocumentDataClassificationResponse
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
    api_instance = formkiq_client.IntelligentDocumentProcessingApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document's data classification
        api_response = api_instance.get_document_data_classification(document_id, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)
        print("The response of IntelligentDocumentProcessingApi->get_document_data_classification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntelligentDocumentProcessingApi->get_document_data_classification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
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

# **get_document_metadata_extraction_results**
> GetDocumentMetadataExtractionResponse get_document_metadata_extraction_results(document_id, llm_prompt_entity_name, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)

Get document's metadata extraction results

Retrieve an document's metadata extraction; available as an Add-On Module.
**Deprecated**. This endpoint is no longer recommended.
Please use **`/documents/{documentId}/ai/prompts/{llmPromptEntityName}`** instead.


### Example


```python
import formkiq_client
from formkiq_client.models.get_document_metadata_extraction_response import GetDocumentMetadataExtractionResponse
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
    api_instance = formkiq_client.IntelligentDocumentProcessingApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    llm_prompt_entity_name = 'llm_prompt_entity_name_example' # str | LlmPrompt Entity Name
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document's metadata extraction results
        api_response = api_instance.get_document_metadata_extraction_results(document_id, llm_prompt_entity_name, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)
        print("The response of IntelligentDocumentProcessingApi->get_document_metadata_extraction_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntelligentDocumentProcessingApi->get_document_metadata_extraction_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **llm_prompt_entity_name** | **str**| LlmPrompt Entity Name | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetDocumentMetadataExtractionResponse**](GetDocumentMetadataExtractionResponse.md)

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
> SetDocumentDataClassificationResponse set_document_data_classification(document_id, site_id=site_id, artifact_id=artifact_id, set_document_data_classification_request=set_document_data_classification_request)

Set document's data classification

Generate Data Classfication attributes within a document; available as an Add-On Module.
**Deprecated**. This endpoint is no longer recommended.
Please use **`/documents/{documentId}/ai/prompts/{llmPromptEntityName}`** instead.


### Example


```python
import formkiq_client
from formkiq_client.models.set_document_data_classification_request import SetDocumentDataClassificationRequest
from formkiq_client.models.set_document_data_classification_response import SetDocumentDataClassificationResponse
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
    api_instance = formkiq_client.IntelligentDocumentProcessingApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    set_document_data_classification_request = formkiq_client.SetDocumentDataClassificationRequest() # SetDocumentDataClassificationRequest |  (optional)

    try:
        # Set document's data classification
        api_response = api_instance.set_document_data_classification(document_id, site_id=site_id, artifact_id=artifact_id, set_document_data_classification_request=set_document_data_classification_request)
        print("The response of IntelligentDocumentProcessingApi->set_document_data_classification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntelligentDocumentProcessingApi->set_document_data_classification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
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

