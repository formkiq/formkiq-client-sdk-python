# openapi_client.TagIndexApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_search**](TagIndexApi.md#index_search) | **POST** /indices/search | 


# **index_search**
> IndexSearchResponse index_search(index_search_request, site_id=site_id, limit=limit, next=next, previous=previous)

Perform a search on a index; this is currently available for both folder and tag indices

### Example


```python
import openapi_client
from openapi_client.models.index_search_request import IndexSearchRequest
from openapi_client.models.index_search_response import IndexSearchResponse
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
    api_instance = openapi_client.TagIndexApi(api_client)
    index_search_request = openapi_client.IndexSearchRequest() # IndexSearchRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)
    previous = 'previous_example' # str | Previous page of results token (optional)

    try:
        api_response = api_instance.index_search(index_search_request, site_id=site_id, limit=limit, next=next, previous=previous)
        print("The response of TagIndexApi->index_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagIndexApi->index_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_search_request** | [**IndexSearchRequest**](IndexSearchRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 
 **previous** | **str**| Previous page of results token | [optional] 

### Return type

[**IndexSearchResponse**](IndexSearchResponse.md)

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

