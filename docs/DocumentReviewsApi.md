# formkiq_client.DocumentReviewsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_review**](DocumentReviewsApi.md#add_document_review) | **POST** /documents/{documentId}/reviews | Add document review
[**add_document_review_decision**](DocumentReviewsApi.md#add_document_review_decision) | **POST** /documents/{documentId}/reviews/{reviewId}/decisions | Add document review decision
[**get_document_review**](DocumentReviewsApi.md#get_document_review) | **GET** /documents/{documentId}/reviews/{reviewId} | Get document review
[**get_document_review_decisions**](DocumentReviewsApi.md#get_document_review_decisions) | **GET** /documents/{documentId}/reviews/{reviewId}/decisions | Get document review decisions
[**get_document_reviews**](DocumentReviewsApi.md#get_document_reviews) | **GET** /documents/{documentId}/reviews | Get document reviews
[**update_document_review**](DocumentReviewsApi.md#update_document_review) | **PATCH** /documents/{documentId}/reviews/{reviewId} | Update document review


# **add_document_review**
> AddDocumentReviewResponse add_document_review(document_id, add_document_review_request, site_id=site_id, artifact_id=artifact_id)

Add document review

Add a review to a document

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_review_request import AddDocumentReviewRequest
from formkiq_client.models.add_document_review_response import AddDocumentReviewResponse
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
    api_instance = formkiq_client.DocumentReviewsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_document_review_request = formkiq_client.AddDocumentReviewRequest() # AddDocumentReviewRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)

    try:
        # Add document review
        api_response = api_instance.add_document_review(document_id, add_document_review_request, site_id=site_id, artifact_id=artifact_id)
        print("The response of DocumentReviewsApi->add_document_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentReviewsApi->add_document_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_document_review_request** | [**AddDocumentReviewRequest**](AddDocumentReviewRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 

### Return type

[**AddDocumentReviewResponse**](AddDocumentReviewResponse.md)

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

# **add_document_review_decision**
> AddDocumentReviewDecisionResponse add_document_review_decision(document_id, review_id, add_document_review_decision_request, site_id=site_id, artifact_id=artifact_id)

Add document review decision

Add a decision to a document review

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_review_decision_request import AddDocumentReviewDecisionRequest
from formkiq_client.models.add_document_review_decision_response import AddDocumentReviewDecisionResponse
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
    api_instance = formkiq_client.DocumentReviewsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    review_id = 'review_id_example' # str | Review Identifier
    add_document_review_decision_request = formkiq_client.AddDocumentReviewDecisionRequest() # AddDocumentReviewDecisionRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)

    try:
        # Add document review decision
        api_response = api_instance.add_document_review_decision(document_id, review_id, add_document_review_decision_request, site_id=site_id, artifact_id=artifact_id)
        print("The response of DocumentReviewsApi->add_document_review_decision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentReviewsApi->add_document_review_decision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **review_id** | **str**| Review Identifier | 
 **add_document_review_decision_request** | [**AddDocumentReviewDecisionRequest**](AddDocumentReviewDecisionRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 

### Return type

[**AddDocumentReviewDecisionResponse**](AddDocumentReviewDecisionResponse.md)

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

# **get_document_review**
> GetDocumentReviewResponse get_document_review(document_id, review_id, site_id=site_id, artifact_id=artifact_id)

Get document review

Get a document review by review id

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_review_response import GetDocumentReviewResponse
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
    api_instance = formkiq_client.DocumentReviewsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    review_id = 'review_id_example' # str | Review Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)

    try:
        # Get document review
        api_response = api_instance.get_document_review(document_id, review_id, site_id=site_id, artifact_id=artifact_id)
        print("The response of DocumentReviewsApi->get_document_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentReviewsApi->get_document_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **review_id** | **str**| Review Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 

### Return type

[**GetDocumentReviewResponse**](GetDocumentReviewResponse.md)

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

# **get_document_review_decisions**
> GetDocumentReviewDecisionsResponse get_document_review_decisions(document_id, review_id, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)

Get document review decisions

Get a listing of decisions for a document review

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_review_decisions_response import GetDocumentReviewDecisionsResponse
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
    api_instance = formkiq_client.DocumentReviewsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    review_id = 'review_id_example' # str | Review Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document review decisions
        api_response = api_instance.get_document_review_decisions(document_id, review_id, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)
        print("The response of DocumentReviewsApi->get_document_review_decisions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentReviewsApi->get_document_review_decisions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **review_id** | **str**| Review Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetDocumentReviewDecisionsResponse**](GetDocumentReviewDecisionsResponse.md)

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

# **get_document_reviews**
> GetDocumentReviewsResponse get_document_reviews(document_id, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)

Get document reviews

Get a listing of reviews for a document

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_reviews_response import GetDocumentReviewsResponse
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
    api_instance = formkiq_client.DocumentReviewsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document reviews
        api_response = api_instance.get_document_reviews(document_id, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)
        print("The response of DocumentReviewsApi->get_document_reviews:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentReviewsApi->get_document_reviews: %s\n" % e)
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

[**GetDocumentReviewsResponse**](GetDocumentReviewsResponse.md)

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

# **update_document_review**
> UpdateResponse update_document_review(document_id, review_id, update_document_review_request, site_id=site_id, artifact_id=artifact_id)

Update document review

Update a document review by review id

### Example


```python
import formkiq_client
from formkiq_client.models.update_document_review_request import UpdateDocumentReviewRequest
from formkiq_client.models.update_response import UpdateResponse
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
    api_instance = formkiq_client.DocumentReviewsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    review_id = 'review_id_example' # str | Review Identifier
    update_document_review_request = formkiq_client.UpdateDocumentReviewRequest() # UpdateDocumentReviewRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)

    try:
        # Update document review
        api_response = api_instance.update_document_review(document_id, review_id, update_document_review_request, site_id=site_id, artifact_id=artifact_id)
        print("The response of DocumentReviewsApi->update_document_review:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentReviewsApi->update_document_review: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **review_id** | **str**| Review Identifier | 
 **update_document_review_request** | [**UpdateDocumentReviewRequest**](UpdateDocumentReviewRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 

### Return type

[**UpdateResponse**](UpdateResponse.md)

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

