# openapi_client.DocumentSharesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_folder_share**](DocumentSharesApi.md#add_folder_share) | **POST** /shares/folders/{indexKey} | Add folder share
[**delete_share**](DocumentSharesApi.md#delete_share) | **DELETE** /shares/{shareKey} | Delete folder share
[**get_user_shares**](DocumentSharesApi.md#get_user_shares) | **GET** /shares | Get user shared folders


# **add_folder_share**
> AddFolderShareResponse add_folder_share(index_key, add_folder_share_request, site_id=site_id)

Add folder share

Creates a new folder share; available as an Add-On Module

### Example


```python
import openapi_client
from openapi_client.models.add_folder_share_request import AddFolderShareRequest
from openapi_client.models.add_folder_share_response import AddFolderShareResponse
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
    api_instance = openapi_client.DocumentSharesApi(api_client)
    index_key = 'index_key_example' # str | Index Key Identifier
    add_folder_share_request = openapi_client.AddFolderShareRequest() # AddFolderShareRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add folder share
        api_response = api_instance.add_folder_share(index_key, add_folder_share_request, site_id=site_id)
        print("The response of DocumentSharesApi->add_folder_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentSharesApi->add_folder_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**| Index Key Identifier | 
 **add_folder_share_request** | [**AddFolderShareRequest**](AddFolderShareRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddFolderShareResponse**](AddFolderShareResponse.md)

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

# **delete_share**
> DeleteShareResponse delete_share(share_key)

Delete folder share

Delete a specific document share; available as an Add-On Module

### Example


```python
import openapi_client
from openapi_client.models.delete_share_response import DeleteShareResponse
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
    api_instance = openapi_client.DocumentSharesApi(api_client)
    share_key = 'share_key_example' # str | Share Identifier

    try:
        # Delete folder share
        api_response = api_instance.delete_share(share_key)
        print("The response of DocumentSharesApi->delete_share:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentSharesApi->delete_share: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **share_key** | **str**| Share Identifier | 

### Return type

[**DeleteShareResponse**](DeleteShareResponse.md)

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

# **get_user_shares**
> GetUserSharesResponse get_user_shares(group=group, limit=limit, next=next)

Get user shared folders

Get a listing of user folder/document shares; available as an Add-On Module

### Example


```python
import openapi_client
from openapi_client.models.get_user_shares_response import GetUserSharesResponse
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
    api_instance = openapi_client.DocumentSharesApi(api_client)
    group = 'group_example' # str | Group Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get user shared folders
        api_response = api_instance.get_user_shares(group=group, limit=limit, next=next)
        print("The response of DocumentSharesApi->get_user_shares:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentSharesApi->get_user_shares: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Group Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetUserSharesResponse**](GetUserSharesResponse.md)

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

