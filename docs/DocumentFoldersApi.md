# formkiq_client.DocumentFoldersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_folder**](DocumentFoldersApi.md#add_folder) | **POST** /folders | Add document folder
[**delete_folder**](DocumentFoldersApi.md#delete_folder) | **DELETE** /folders/{indexKey} | Delete document folder
[**get_folder_documents**](DocumentFoldersApi.md#get_folder_documents) | **GET** /folders | Get document folders


# **add_folder**
> AddFolderResponse add_folder(add_folder_request, site_id=site_id, share_key=share_key)

Add document folder

Creates a new folder

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.add_folder_request import AddFolderRequest
from formkiq_client.models.add_folder_response import AddFolderResponse
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
    api_instance = formkiq_client.DocumentFoldersApi(api_client)
    add_folder_request = formkiq_client.AddFolderRequest() # AddFolderRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Add document folder
        api_response = api_instance.add_folder(add_folder_request, site_id=site_id, share_key=share_key)
        print("The response of DocumentFoldersApi->add_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentFoldersApi->add_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_folder_request** | [**AddFolderRequest**](AddFolderRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**AddFolderResponse**](AddFolderResponse.md)

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

# **delete_folder**
> DeleteFolderResponse delete_folder(index_key, site_id=site_id, share_key=share_key)

Delete document folder

Delete a specific folder; folder must be empty

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.delete_folder_response import DeleteFolderResponse
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
    api_instance = formkiq_client.DocumentFoldersApi(api_client)
    index_key = 'index_key_example' # str | Index Key Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Delete document folder
        api_response = api_instance.delete_folder(index_key, site_id=site_id, share_key=share_key)
        print("The response of DocumentFoldersApi->delete_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentFoldersApi->delete_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index_key** | **str**| Index Key Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**DeleteFolderResponse**](DeleteFolderResponse.md)

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

# **get_folder_documents**
> GetFoldersResponse get_folder_documents(site_id=site_id, index_key=index_key, limit=limit, share_key=share_key, next=next)

Get document folders

Get list of documents in a folder

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.get_folders_response import GetFoldersResponse
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
    api_instance = formkiq_client.DocumentFoldersApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    index_key = 'index_key_example' # str | Index Key Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    share_key = 'share_key_example' # str | Share Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document folders
        api_response = api_instance.get_folder_documents(site_id=site_id, index_key=index_key, limit=limit, share_key=share_key, next=next)
        print("The response of DocumentFoldersApi->get_folder_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentFoldersApi->get_folder_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **index_key** | **str**| Index Key Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **share_key** | **str**| Share Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetFoldersResponse**](GetFoldersResponse.md)

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

