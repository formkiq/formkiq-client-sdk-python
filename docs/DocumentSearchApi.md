# formkiq_client.DocumentSearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_search**](DocumentSearchApi.md#document_search) | **POST** /search | Document search


# **document_search**
> DocumentSearchResponse document_search(document_search_request, site_id=site_id, limit=limit, next=next, previous=previous)

Document search

Document search query request;   Supports searching DynamoDB for document(s) by a single TAG key and/or value. Value can be \"exacted\" or \"begins_with\" matched. Search can be filtered to only check certain documentIds (up to 100 documentIds accepted).  If using Enteprise TagSchema Composite Keys feature then multiple tag(s) can be searched for.  If Typesense is enabled, full text search is supported through the \"text\" parameter. Full text search will look for the text in the \"content\" and/or document \"metadata\".  DocumentIds parameter allows you to filter your results to a specific set of documents.   See requestBody examples below for commmon examples.

### Example


```python
import formkiq_client
from formkiq_client.models.document_search_request import DocumentSearchRequest
from formkiq_client.models.document_search_response import DocumentSearchResponse
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
    api_instance = formkiq_client.DocumentSearchApi(api_client)
    document_search_request = {"query":{"tag":{"key":"category"}}} # DocumentSearchRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)
    previous = 'previous_example' # str | Previous page of results token (optional)

    try:
        # Document search
        api_response = api_instance.document_search(document_search_request, site_id=site_id, limit=limit, next=next, previous=previous)
        print("The response of DocumentSearchApi->document_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentSearchApi->document_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_search_request** | [**DocumentSearchRequest**](DocumentSearchRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 
 **previous** | **str**| Previous page of results token | [optional] 

### Return type

[**DocumentSearchResponse**](DocumentSearchResponse.md)

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

