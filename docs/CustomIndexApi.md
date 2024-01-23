# formkiq_client.CustomIndexApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_index**](CustomIndexApi.md#delete_index) | **DELETE** /indices/{indexType}/{indexKey} | 
[**index_folder_move**](CustomIndexApi.md#index_folder_move) | **POST** /indices/{indexType}/move | 
[**index_search**](CustomIndexApi.md#index_search) | **POST** /indices/search | 


# **delete_index**
> DeleteIndicesResponse delete_index(index_key, index_type, site_id=site_id)



Perform a delete on the Folder Index

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.delete_indices_response import DeleteIndicesResponse
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
    api_instance = formkiq_client.CustomIndexApi(api_client)
    index_key = 'index_key_example' # str | Index Key Identifier
    index_type = 'index_type_example' # str | Index Type
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        api_response = api_instance.delete_index(index_key, index_type, site_id=site_id)
        print("The response of CustomIndexApi->delete_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomIndexApi->delete_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**| Index Key Identifier | 
 **index_type** | **str**| Index Type | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteIndicesResponse**](DeleteIndicesResponse.md)

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

# **index_folder_move**
> IndexFolderMoveResponse index_folder_move(index_type, index_folder_move_request, site_id=site_id)



Perform an Folder Index Move

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.index_folder_move_request import IndexFolderMoveRequest
from formkiq_client.models.index_folder_move_response import IndexFolderMoveResponse
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
    api_instance = formkiq_client.CustomIndexApi(api_client)
    index_type = 'index_type_example' # str | Index Type
    index_folder_move_request = formkiq_client.IndexFolderMoveRequest() # IndexFolderMoveRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        api_response = api_instance.index_folder_move(index_type, index_folder_move_request, site_id=site_id)
        print("The response of CustomIndexApi->index_folder_move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomIndexApi->index_folder_move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_type** | **str**| Index Type | 
 **index_folder_move_request** | [**IndexFolderMoveRequest**](IndexFolderMoveRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**IndexFolderMoveResponse**](IndexFolderMoveResponse.md)

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

# **index_search**
> IndexSearchResponse index_search(index_search_request, site_id=site_id, limit=limit, next=next, previous=previous)



Perform a search on a index; this is currently available for both folder and tag indices

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.index_search_request import IndexSearchRequest
from formkiq_client.models.index_search_response import IndexSearchResponse
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
    api_instance = formkiq_client.CustomIndexApi(api_client)
    index_search_request = formkiq_client.IndexSearchRequest() # IndexSearchRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)
    previous = 'previous_example' # str | Previous page of results token (optional)

    try:
        api_response = api_instance.index_search(index_search_request, site_id=site_id, limit=limit, next=next, previous=previous)
        print("The response of CustomIndexApi->index_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomIndexApi->index_search: %s\n" % e)
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

